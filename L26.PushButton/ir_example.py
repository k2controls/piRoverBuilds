''' Demonstrating infrared as input
Note: This demo requires and infrared device 
to test. Additionally, a jumper is required on the 
Arduino function switch - see hardware documentation.

Keith E. Kelly
10/10/20
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants to represent piRover LED pin numbers
RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 18
#create constants to represent piRover pushbutton pin number
IR_PIN = 3

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set pin LED pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
# Set IR pin as input
GPIO.setup(IR_PIN, GPIO.IN)

print("This solution demonstrates the IR sensor as an input.")
print("You need an IR transmitter like tv remote.")
print()
print("Press a button on the remote to light the LEDs")

while True:
    #get state of IR in and update LEDs
    state = GPIO.input(IR_PIN)
    print(state)
    #wait for pin to go low
    #pulses so we need to read frequently
    while state == 1:
        state = GPIO.input(IR_PIN)
        time.sleep(.1)
    print("Pulse detected")
    #IR key was press so light LED for 1 sec      
    GPIO.output(RED_PIN, True)
    GPIO.output(GREEN_PIN, True)
    GPIO.output(BLUE_PIN, True)
    time.sleep(1)
    #turn off and start again
    GPIO.output(RED_PIN, False)
    GPIO.output(GREEN_PIN, False)
    GPIO.output(BLUE_PIN, False)
    time.sleep(1)

