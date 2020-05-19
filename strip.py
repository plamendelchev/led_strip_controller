import RPi.GPIO as GPIO

class Strip():
    def __init__(self, channels, frequency=100):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channels, GPIO.OUT)

        self.frequency = frequency
        self._red = GPIO.PWM(channels[0], self.frequency)
        self._green = GPIO.PWM(channels[1], self.frequency)
        self._blue = GPIO.PWM(channels[2], self.frequency)
        #self._white = GPIO.PWM(channels[3], self.frequency)

    @property
    def red(self):
        return self._red
    @red.setter
    def red(self, value):
        self._red.ChangeDutyCycle(value)

    @property
    def green(self):
        return self._green
    @green.setter
    def green(self, value):
        self._green.ChangeDutyCycle(value)

    @property
    def blue(self):
        return self._blue
    @blue.setter
    def blue(self, value):
        self._blue.ChangeDutyCycle(value)
    """
    @property
    def white(self):
        return self._white
    @white.setter
    def white(self, value):
        self._white.ChangeDutyCycle(value)
    """
    def on(self):
        default_brightness = 100
        self.red.start(default_brightness)
        self.green.start(default_brightness)
        self.blue.start(default_brightness)
        #self.white.start(default_brightness)

    def off(self):
        self.red.stop()
        self.green.stop()
        self.blue.stop()
        #self.white.stop()

    def color(self, r=0, g=0, b=0, w=0):
        self.red = r
        self.green = g
        self.blue = b
        #self.white = w
