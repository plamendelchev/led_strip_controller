import RPi.GPIO as GPIO
from helpers import to_rgb, is_white

class Strip():
    channels = (12, 13, 18, 19)
    _color = '#000000'
    _intensity = 0.5
    _status = 'off'

    def __init__(self):
        # GPIO Initial Settings
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channels, GPIO.OUT)

        # Dictionary with all LED colors (keys) and their GPIO.PWM objects (values)
        freq = 100
        self.leds = {'red': GPIO.PWM(self.channels[0], freq),
                    'green': GPIO.PWM(self.channels[1], freq),
                    'blue': GPIO.PWM(self.channels[2], freq),
                    'white': GPIO.PWM(self.channels[3], freq)}

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if value == 'on': 
            if not self.color == '#00000' and self.status == 'off':
                self.on(self.color)
            else:
                self.color = self.color
        else:
            self.off()
        self._status = value

    @property
    def intensity(self):
        return self._intensity
    @intensity.setter
    def intensity(self, value):
        self._intensity = value
        self.color = self.color

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        r, g, b = to_rgb(value, self.intensity)
        if is_white(value):
            self.leds['white'].ChangeDutyCycle(100 * self.intensity)
            self.leds['red'].ChangeDutyCycle(0)
            self.leds['green'].ChangeDutyCycle(0)
            self.leds['blue'].ChangeDutyCycle(0)
        else:
            self.leds['white'].ChangeDutyCycle(0)
            self.leds['red'].ChangeDutyCycle(r)
            self.leds['green'].ChangeDutyCycle(g)
            self.leds['blue'].ChangeDutyCycle(b)
        self._color = value

    def on(self, value):
        r, g, b = to_rgb(value, self.intensity)
        if is_white(value):
            self.leds['white'].start(100 * self.intensity)
            self.leds['red'].start(0)
            self.leds['green'].start(0)
            self.leds['blue'].start(0)
        else:
            self.leds['white'].start(0)
            self.leds['red'].start(r)
            self.leds['green'].start(g)
            self.leds['blue'].start(b)

    def off(self):
        for led in self.leds.values():
            led.stop()

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
