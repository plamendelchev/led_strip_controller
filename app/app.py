from flask import Flask, request
from models import Strip
from helpers import valid_data, valid_status, valid_color, valid_intensity

app = Flask(__name__)

strip = Strip()

@app.route("/")
def default():
    return 'stana goshoooo\n'

@app.route("/strip", methods=['GET'])
def get():
    return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }

@app.route("/strip", methods=['POST'])
def set():
    data = request.get_json()
    if not valid_data(data.keys()):
        return {"error": "Invalid data keys"}

    if 'intensity' in data:
        if valid_intensity(data['intensity']):
            strip.intensity = data['intensity']
        else:
            return {'error': 'Invalid intensity'}, 400
    if 'color' in data:
        if valid_color(data['color']):
            strip.color = data['color']
        else:
            return {'error': 'Invalid data'}, 400
    if 'status' in data:
        if valid_status(data['status']):
            strip.status = data['status']
        else:
            return {'error': 'Invalid status'}, 400

    return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }
