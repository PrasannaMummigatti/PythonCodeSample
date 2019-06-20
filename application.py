from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Prasanna New test from my laptop!"
