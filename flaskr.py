import sqlite3
from flask import Flask, g

#configurações

DATABASE = './flaskr.db'
SECRET_KEY = "pudim"
USER = "admin"
PASSWORD = "senha"

#APLICACAO

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_first_request
def before():
    g.db = connect_db()

@app.teardown_request
def after(exception):
    g.db.close()

@app.route('/')
def index():
    return "<h1>Hello World, George</h1>"

