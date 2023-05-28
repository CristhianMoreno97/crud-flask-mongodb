from flask import Blueprint, render_template

blueprint = Blueprint('home', __name__, url_prefix='/')

@blueprint.route('/')
def home() -> str:
    return render_template('index.html')