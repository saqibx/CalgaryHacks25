import io
import PyPDF2
from bson import ObjectId
from dotenv import load_dotenv
from flask import session


import RentersMethods.Instructions
from config import Config
# from routes.renters import *
from extensions import *
from google import genai

import os

load_dotenv()
GEMINI_API_KEY = Config.GEMINI_KEY
client = genai.Client(api_key=GEMINI_API_KEY)


def pdf_to_text(file_id):

    # Convert file_id to ObjectId if necessary
    if isinstance(file_id, str):
        file_id = ObjectId(file_id)

    # Retrieve the file from GridFS using the existing GridFS instance 'fs'
    grid_out = fs.get(file_id)

    # Read PDF data into an in-memory bytes stream
    pdf_data = grid_out.read()
    pdf_stream = io.BytesIO(pdf_data)

    # Parse the PDF using PyPDF2
    reader = PyPDF2.PdfReader(pdf_stream)

    # Extract text from each page of the PDF
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "  # Add a space between pages

    # Post-process: collapse all whitespace (newlines, extra spaces) into single spaces.
    compact_text = ' '.join(text.split())

    instructions = RentersMethods.Instructions.instructions + " DO NOT INCLUDE THINGS LIKE Okay, here's the expert analysis of the provided rental agreement, adhering to the constraints specified:"
    location_details = f"This person is from {session.get('location')}, so make the provincial laws specific to this location"
    compact_text = f'{instructions} \n{compact_text} {location_details}'
    return compact_text

def feed(content):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=content,
    )
    return response.text

def finalized_analysis():
    file_id = session.get('file_id')
    # file_id = "67b157cb7ed72fcc68490368"
    text = pdf_to_text(file_id)
    return (feed(text))


# finalized_analysis()