from flask import Flask
from views import home_view, computers_view

app = Flask(__name__)
app.register_blueprint(home_view.home_blueprint)
app.register_blueprint(computers_view.computer_blueprint)

def run_app():
    app.run(debug=True, port=4000)

if __name__ == '__main__':
    run_app()