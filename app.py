from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass


app = Flask(__name__)
app.config.from_object('config.DevConfig')
db = SQLAlchemy(model_class=Base)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pingpong")
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })