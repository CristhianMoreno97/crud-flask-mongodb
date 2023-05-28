from flask import Blueprint, render_template

home_blueprint = Blueprint('home', __name__, url_prefix='/')

@home_blueprint.route('/')
def home() -> str:
    return render_template('index.html')