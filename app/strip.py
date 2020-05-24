import RPi.GPIO as GPIO
from colors import to_rgb, is_white

class Strip():
    channels = (12, 13, 18, 19)

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
            if self.status == 'off' and not self.color == '#00000':
                self.on(self.color)
            else:
                self.color = self.color
        elif value == 'off':
            self.off()
        self._status = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        r, g, b = to_rgb(value)
        if is_white(value):
            self.leds['white'].ChangeDutyCycle(100)
            self.leds['red'].ChangeDutyCycle(0)
            self.leds['green'].ChangeDutyCycle(0)
            self.leds['blue'].ChangeDutyCycle(0)
        else:
            self.leds['white'].ChangeDutyCycle(0)
            self.leds['red'].ChangeDutyCycle(r)
            self.leds['green'].ChangeDutyCycle(g)
            self.leds['blue'].ChangeDutyCycle(b)
        self._color = value

    # Turn on all LEDs
    def on(self, value):
        r, g, b = to_rgb(value)
        if is_white(value):
            self.leds['white'].start(100)
            self.leds['red'].start(0)
            self.leds['green'].start(0)
            self.leds['blue'].start(0)
        else:
            self.leds['white'].start(0)
            self.leds['red'].start(r)
            self.leds['green'].start(g)
            self.leds['blue'].start(b)

    # Turn off all LEDs
    def off(self):
        self.leds['white'].stop()
        self.leds['red'].stop()
        self.leds['green'].stop()
        self.leds['blue'].stop()

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
