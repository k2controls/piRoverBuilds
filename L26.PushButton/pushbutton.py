''' Pushbutton Solution
Keith E. Kelly
10/4/20
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants to represent piRover LED pin numbers
RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 18
#create constants to represent piRover pushbutton pin number
PB_PIN = 24

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set pin LED pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
# Set pushbutton pin as input
GPIO.setup(PB_PIN, GPIO.IN)

while True:
    #get state of pin and update LEDs
    state = GPIO.input(PB_PIN)
    if state == True:  #active low
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, False)
    else:
        GPIO.output(RED_PIN, True)
        GPIO.output(GREEN_PIN, True)
        GPIO.output(BLUE_PIN, True)
    time.sleep(.1)