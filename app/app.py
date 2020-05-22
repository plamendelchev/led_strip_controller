from flask import Flask
from strip import Strip

app = Flask(__name__)

@app.route("/")
def default():
    return 'stana goshoooo\n'
