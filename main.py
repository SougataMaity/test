
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!\nits a first flask prigramprogram\nyou dont know please follow<p>"

@app.route("/first")
def hp():
    return "My name sougata\nI am a sp person"

@app.route("/sc")
def sc():
    return "you are a sc boy"

if __name__ ==  "__main__":
    app.run(debug=True)