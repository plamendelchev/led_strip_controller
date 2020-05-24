import RPi.GPIO as GPIO
from PIL import ImageColor

class Strip():
    def __init__(self):
        # GPIO Channels
        channels = (12, 13, 18, 19)

        # GPIO Initial Settings
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channels, GPIO.OUT)

        # Dictionary with all LED colors (keys) and their GPIO.PWM objects (values)
        self.leds = {'red': None, 'green': None, 'blue': None, 'white': None}
        # Populate dict with GPIO.PWN objects
        for channel, color in zip(channels, self.leds): 
            self.leds[color] = GPIO.PWM(channel, 100)

        # status instance attribute
        self.status = 'off'
        #self.color = 'FFFFFF'

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value == 'on':
            self.on()
        elif value == 'off':
            self.off()
        self._status = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        r, g, b = [int(round(i*100/256)) for i in ImageColor.getrgb('#' + value)]
        self._color = value

    # Turn on all LEDs
    def on(self, brightness=50):
        for led in self.leds.values():
            led.start(brightness)

    # Turn off all LEDs
    def off(self):
        for led in self.leds.values():
            led.stop()
    
    """
    # Set a specific color to the whole strip == set a specific color to a specific LED
    def color(self, r, g, b, w):
        self.leds['red'].ChangeDutyCycle(r)
        self.leds['green'].ChangeDutyCycle(g)
        self.leds['blue'].ChangeDutyCycle(b)
        self.leds['white'].ChangeDutyCycle(w)
    """

    # Set a specific PWM frequency to the whole strip == change the frequency of each individual LED
    def frequency(self, r, g, b, w):
        self.leds['red'].ChangeFrequency(r)
        self.leds['green'].ChangeFrequency(g)
        self.leds['blue'].ChangeFrequency(b)
        self.leds['white'].ChangeFrequency(w)

    # Turn off all leds and set all GPIO pins to LOW
    def poweroff(self):
        self.off()
        GPIO.cleanup()
