import re

def valid_data(data):
    valid_headers = ('status', 'color', 'intensity')
    if [h for h in data if h in valid_headers]:
        return True
    else:
        return False

def valid_status(data):
    if data == 'on' or data == 'off' or data == 'startup' or data == 'poweroff':
        return True
    else:
        return False

def valid_color(data):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', data)
    if match:
        return True
    else:
        return False

def valid_intensity(data):
    if 0 <= data <= 1:
        return True
    else:
        return False
