import json

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, Response
import gridfs
from bson.objectid import ObjectId
from flask_wtf import file

import RentersMethods.deepseek_analysis
from extensions import fs, db
from RentersMethods import *

renters_bp = Blueprint("renters", __name__)

@renters_bp.route("/renters", methods=["GET", "POST"])
def renters():
    if "user" not in session:
        flash("You must be logged in to upload files!", "danger")
        return redirect(url_for("login.login"))

    username = session["user"]
    uploaded_files = list(db.uploads.find({"username": username}))
    print(uploaded_files)

    return render_template("renters.html", uploaded_files=uploaded_files)

@renters_bp.route("/renters_analysis", methods=["POST"])
def renters_analysis():
    if "lease" not in request.files:
        flash("No file uploaded. Please upload again.", "danger")
        return redirect(url_for("renters.renters"))

    file = request.files["lease"]
    flash(file.filename)
    if file.filename == "":
        flash("No selected file", "danger")
        return redirect(url_for("renters.renters"))

    username = session["user"]

    province = request.form.get('province')
    if province:
        session['location'] = province
    else:
        session['location'] = "Canada"

    file_id = fs.put(file, filename=file.filename, username=username)
    session['file_id'] = str(file_id)
    db.uploads.insert_one({
        "username": username,
        "file_id": file_id,
        "filename": file.filename
    })

    flash("Successfully uploaded!", "success")
    return redirect(url_for("renters.display_analysis"))

@renters_bp.route("/renters_previous/<file_id>", methods=["GET"])
def renters_previous(file_id):
    username = session.get("username")
    session['file_id'] = str(file_id)

    return redirect(url_for("renters.display_analysis"))

@renters_bp.route("/download_files", methods=["GET", "POST"])
def download_files():
    return "under const"

# def user_files():
#     username = session.get('user')
#     user_files = list(db.uploads.find({"username":username}))


def get_file_content(file_id):
    try:
        file = fs.get(ObjectId(file_id))
        content = file.read()
        return content
    except Exception as e:
        print(f"Error retrieving file: {e}")
        return None


@renters_bp.route('/analysis')
def display_analysis():
    data = RentersMethods.deepseek_analysis.finalized_analysis()
    print("Gemini output:", data)  # Debug print


    if data.startswith("```json"):
        data = data.split("```json", 1)[1]
        if "```" in data:
            data = data.split("```", 1)[0].strip()

    if not data.strip():
        flash("Analysis returned an empty response.", "danger")
        return redirect(url_for("renters.renters"))


    try:
        analysis_data = json.loads(data)
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
        flash("Error parsing analysis response.", "danger")
        return redirect(url_for("renters.renters"))
    # Pass the dictionary to your template
    return render_template('display.html', analysis=analysis_data)
