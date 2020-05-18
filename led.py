class Led():
    def __init__(self, red=0, blue=0, green=0, white=0):
        self.red = red
        self.blue = blue
        self.green = green
        self.white = white

    def __str__(self):
        return f'Red: {self.red}, Blue: {self.blue}, Green: {self.green}, White: {self.white}'
