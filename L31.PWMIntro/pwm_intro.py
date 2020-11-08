''' Pulse Width Modulation (PWM) introduction
LED module is used to demonstrate use and control
of PWM output results.

Keith E. Kelly
11/7/20
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants for LED GPIO pin
RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 18

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set LED as output
GPIO.setup(RED_PIN, GPIO.OUT, initial=False)
GPIO.setup(GREEN_PIN, GPIO.OUT, initial=False)
GPIO.setup(BLUE_PIN, GPIO.OUT, initial=False)

### Example 1 ###
# Set Red LED as PWM to blink
# Adjust both frequency and duty cycle to investigate
freq = 1
dc = 50
pwm_red = GPIO.PWM(RED_PIN, freq)
pwm_red.start(dc)
while(True):
    pass