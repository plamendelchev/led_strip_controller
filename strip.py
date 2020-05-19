import RPi.GPIO as GPIO

class Strip():
    def __init__(self, channels):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(channels, GPIO.OUT)

        self._red = GPIO.PWM(channels[0], 100)
        self._green = GPIO.PWM(channels[1], 100)
        self._blue = GPIO.PWM(channels[2], 100)
        self._white = GPIO.PWM(channels[3], 100)

    def on(self, brightness=50):
        self._red.start(brightness)
        self._green.start(brightness)
        self._blue.start(brightness)
        self._white.start(brightness)

    def off(self):
        self._red.stop()
        self._green.stop()
        self._blue.stop()
        self._white.stop()

    def color(self, r, g, b, w):
        self._red.ChangeDutyCycle(r)
        self._green.ChangeDutyCycle(g)
        self._blue.ChangeDutyCycle(b)
        self._white.ChangeDutyCycle(w)

    def frequency(self, r, g, b, w):
        self._red.ChangeFrequency(r)
        self._green.ChangeFrequency(g)
        self._blue.ChangeFrequency(b)
        self._white.ChangeFrequency(w)

    def poweroff(self):
        self.off()
        GPIO.cleanup()
