from flask import Flask, request
from strip import Strip

app = Flask(__name__)
strip = Strip()

def valid_status(data):
    if data == 'on' or data == 'off':
        return True
    else:
        return False

# Add validation for data.length == 6
def valid_color(data):
    try:
        int(data, 16)
        return True
    except ValueError:
        return False

def valid_data(data):
    valid_headers = ('status', 'color', 'intensity')
    if [h for h in data if h in valid_headers]:
        return True
    else:
        return False

@app.route("/")
def default():
    return 'stana goshoooo\n'

@app.route("/strip", methods=['GET'])
def get():
    #return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }
    return {"status": strip.status }

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

    return {"status": strip.status, "color": strip.color}
    #return {"status": strip.status, "color": strip.color, "intensity": strip.intensity }
