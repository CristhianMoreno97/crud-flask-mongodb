from flask import Blueprint, render_template, request, Response, jsonify, redirect
from database import connection
from models.computer import Computer

computer_blueprint = Blueprint("computers", __name__, url_prefix="/computers")
db = connection.Database()
db.connect()

@computer_blueprint.route("", methods=["GET"])
def getComputers() -> str:
    computers = db.getCollection("computers")
    computers_data = computers.find()
    return render_template("computers.html", computers_data=computers_data)

@computer_blueprint.route("/edit/<string:computer_name>", methods=["GET"])
def editComputer(computer_name: str) -> str:
    computers = db.getCollection("computers")
    computer = computers.find_one({"name": computer_name})
    print(computer)
    if computer:
        return render_template("edit_computer.html", computer=computer)
    else:
        return Response("Computer not found", status=404)
    
@computer_blueprint.route("/edit/<string:computer_name>", methods=["POST"])
def editComputerPost(computer_name: str) -> str:
    computers = db.getCollection("computers")
    computer = computers.find_one({"name": computer_name})
    if computer:
        name = request.form["name"]
        brand = request.form["brand"]
        price = request.form["price"]
        color = request.form["color"]
        memory = request.form["memory"]
        storage = request.form["storage"]
        processor = request.form["processor"]
        category = request.form["category"]
        description = request.form["description"]
        image_url = request.form["image_url"]
        stock = request.form["stock"]

        if name:
            try:
                computer = Computer(
                    name,
                    brand,
                    price,
                    color,
                    memory,
                    storage,
                    processor,
                    category,
                    description,
                    image_url,
                    stock,
                )
                computers.update_one({"name": computer_name}, {"$set": computer.toDBCollection()})
                return redirect("/computers")
            except Exception as e:
                print(f"Error editing computer: {str(e)}")
    else:
        return Response("Computer not found", status=404)

@computer_blueprint.route("/add", methods=["GET"])
def addComputerForm() -> str:
    return render_template("add_computer.html")

@computer_blueprint.route("/add", methods=["POST"])
def addComputer() -> str:
    computers = db.getCollection("computers")
    name = request.form["name"]
    brand = request.form["brand"]
    price = request.form["price"]
    color = request.form["color"]
    memory = request.form["memory"]
    storage = request.form["storage"]
    processor = request.form["processor"]
    category = request.form["category"]
    description = request.form["description"]
    image_url = request.form["image_url"]
    stock = request.form["stock"]

    if name:
        try:
            computer = Computer(
                name,
                brand,
                price,
                color,
                memory,
                storage,
                processor,
                category,
                description,
                image_url,
                stock,
            )
            computers.insert_one(computer.toDBCollection())
            return redirect("/computers/add")
        except Exception as e:
            print(f"Error adding computer: {str(e)}")