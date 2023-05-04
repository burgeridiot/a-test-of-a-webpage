import flask
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def rban():     
    return flask.render_template("home")
@app.route("/banlist")
def returnban():
    return "{12345678910, 10987654321} --dban"
