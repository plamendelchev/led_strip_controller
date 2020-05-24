from flask import Flask, request
from strip import Strip
from validator import valid_data, valid_status, valid_color, valid_intensity

app = Flask(__name__)

strip = Strip()
strip.status = 'off'
strip.color = '#000000'

@app.route("/")
def default():
    return 'stana goshoooo\n'

@app.route("/strip", methods=['GET'])
def get():
    #return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }
    return {"status": strip.status, "color": strip.color}

@app.route("/strip", methods=['POST'])
def set():
    data = request.get_json()
    if not valid_data(data.keys()):
        return {"error": "Invalid data keys"}

    if 'status' in data:
        if valid_status(data['status']):
            strip.status = data['status']
        else:
            return {'error': 'Invalid status'}, 400
    if 'color' in data:
        if valid_color(data['color']):
            strip.color = data['color']
        else:
            return {'error': 'Invalid data'}, 400
    if 'intensity' in data:
        if valid_intensity(data['intensity']):
            strip.intensity = data['intensity']
        else:
            return {'error': 'Invalid intensity'}, 400

    return {'status': strip.status, 'color': strip.color}
    #return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }
