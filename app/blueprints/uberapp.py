from flask import Blueprint, render_template



app_bp = Blueprint("uberapp",__name__)


@app_bp.route("/")
def index():
    return render_template("index.html")

@app_bp.route("/login")
def login_form():
    return render_template("login_form.html")