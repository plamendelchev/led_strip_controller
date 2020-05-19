import RPi.GPIO as GPIO

class Led(GPIO):
    def __init__(self, channel, brightness, frequency):
        self.channel = channel
        self.brightness = brightness
        self.frequency = frequency

        self.PWM(self.channel, self.frequency)
