from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
        {"name": "oranges", "quantity": 2},
        {"name": "strawberries", "quantity": 6},
        {"name": "grapes", "quantity": 12}
    ]
    return render_template("index.html", fruits=fruits)