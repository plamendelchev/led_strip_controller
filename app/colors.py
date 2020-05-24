from PIL import ImageColor

def to_rgb(value, intensity):
    rgb = [int(round(i * 100 / 256)) for i in ImageColor.getrgb(value)]
    return [i * intensity for i in rgb]

def is_white(value):
    if value == '#FFFFFF':
        return True
    else:
        return False
