from PIL import ImageColor

def to_rgb(value):
    return [int(round(i*100/256)) for i in ImageColor.getrgb(value)]

def is_white(value):
    if value == '#FFFFFF':
        return True
    else:
        return False
