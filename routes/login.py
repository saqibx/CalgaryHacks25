from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

from extensions import users_collection

login_bp = Blueprint("login", __name__)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = users_collection.find_one({"username": form.username.data})
        if user and user["password"] == form.password.data:
            session["user"] = form.username.data
            flash("Login successful!", "success")
            return redirect(url_for("renters.renters"))
        flash("Invalid username or password", "danger")
    return render_template("login.html", form=form)

@login_bp.route("/register", methods=["GET", "POST"])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        if users_collection.find_one({"username": form.username.data}):
            flash("Username already exists!", "danger")
        else:
            users_collection.insert_one({"username": form.username.data, "password": form.password.data})
            #flash("Registration successful! Please log in.", "success")
            return redirect(url_for("renters.renters"))
    return render_template("register.html", form=form)
