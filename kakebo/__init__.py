from flask import Flask

app = Flask(__name__, instance_relative_config=True) #la vamos a sacar del código
app.config.from_object("config")

from kakebo import views

