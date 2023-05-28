from flask import Blueprint, render_template

computer_blueprint = Blueprint('computers', __name__, url_prefix='/computers')

@computer_blueprint.route('', methods=['GET'])
def getComputers() -> str:
    return render_template('computers.html')