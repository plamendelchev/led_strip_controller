import RPi.GPIO as GPIO
from time import sleep

channels = (12, 13, 18, 19)

default_brightness = 50
default_frequency = 100

def initialize_leds():
    GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
    GPIO.setwarnings(False)         # Supressing wanring messages
    GPIO.setup(channels, GPIO.OUT)   # Declaring channels to be used

    led_red = GPIO.PWM(channels[1], default_frequency)    # Created a PWM object
    led_green = GPIO.PWM(channels[2], default_frequency)    # Created a PWM object
    led_blue = GPIO.PWM(channels[3], default_frequency)    # Created a PWM object
    led_white = GPIO.PWM(channels[4], default_frequency)    # Created a PWM object

    return led_red, led_green, led_blue, led_white

leds = initialize_leds()

def set_color(r, b, g):
    if all(values == 255 for values in leds):
        for color in leds:
            leds[color] = 0
        led_white = 255
    else:
        led_red.ChangeDutyCycle(r)
        led_blue.ChangeDutyCycle(b)
        led_green.ChangeDutyCycle(g)

def on():
    pwm.start(default_brightness)
    print('Led is on')

def off():
    pwm.stop()
    print('Led is off')

def set_brightness(num):
    pwm.ChangeDutyCycle(num)
    print(f'Brightness changed to {num}')
