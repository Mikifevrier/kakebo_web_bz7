from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hola"

@app.route("/adios")
def bye():
    return "Hasta luego"