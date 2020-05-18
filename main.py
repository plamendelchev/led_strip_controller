import RPi.GPIO as GPIO
from time import sleep

led_pin = 18
default_brightness = 50
default_frequency = 100

def initialize_pwm():
    GPIO.setmode(GPIO.BCM)          # We are using the BCM pin numbering
    GPIO.setwarnings(False)
    GPIO.setup(led_pin, GPIO.OUT)   # Declaring pin 18 as output pin
    pwm = GPIO.PWM(led_pin, default_frequency)    # Created a PWM object
    return pwm

pwm = initialize_pwm()

def on():
    pwm.start(default_brightness)
    print('Led is on')

def off():
    pwm.stop()
    print('Led is off')

def set_brightness(num):
    pwm.ChangeDutyCycle(num)
    print(f'Brightness changed to {num}')
