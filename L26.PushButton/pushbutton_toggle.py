''' Pushbutton Toggle using while to check for button release
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

print("This solution demonstrates waiting for PB release to toggle the LEDs.")
print()
print("Press the pushbutton to toggle the LEDs.")

switch_state = True #active low - is high until pushed
lamp_on = False
# toggle light 10 times and then stop
count = 0

while count < 10:
    #wait for push
    while switch_state == True:
        switch_state = GPIO.input(PB_PIN)
    #wait for release
    while switch_state == False:
        switch_state = GPIO.input(PB_PIN)
    # switch has been released - update push count
    count = count + 1
    print(count)
    if not lamp_on:
        # turn lamps on
        GPIO.output(RED_PIN, True)
        GPIO.output(GREEN_PIN, True)
        GPIO.output(BLUE_PIN, True)
        # update variable tracking lamp status
        lamp_on = True
    else:
        # turn lamps off
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, False)
        # update variable tracking lamp status
        lamp_on = False

GPIO.cleanup()