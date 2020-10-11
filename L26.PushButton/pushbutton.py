''' Demonstrating GPIO input using piRover Pushbutton
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

print("This pushbutton solution demonstrates the use of a GPIO as an input,")
print()
print("Press the pushbutton on the controller board to light the LEDs.")
while True:
    #get state of pin and update LEDs
    state = GPIO.input(PB_PIN)
    if state == True:  #switch is active low
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, False)
    else:
        GPIO.output(RED_PIN, True)
        GPIO.output(GREEN_PIN, True)
        GPIO.output(BLUE_PIN, True)
    time.sleep(.1)

# Note that the state variable is not required
# You can call the input function in the if statement
# while True:
#     if GPIO.input(PB_PIN):  #switch is active low
#         GPIO.output(RED_PIN, False)
#         GPIO.output(GREEN_PIN, False)
#         GPIO.output(BLUE_PIN, False)
#     else:
#         GPIO.output(RED_PIN, True)
#         GPIO.output(GREEN_PIN, True)
#         GPIO.output(BLUE_PIN, True)
#     time.sleep(.1)

# Let's try to make the switch only work 10 times
# count = 0
# while count < 10:
#     if GPIO.input(PB_PIN):  #switch is active low
#         GPIO.output(RED_PIN, False)
#         GPIO.output(GREEN_PIN, False)
#         GPIO.output(BLUE_PIN, False)
#     else:
#         GPIO.output(RED_PIN, True)
#         GPIO.output(GREEN_PIN, True)
#         GPIO.output(BLUE_PIN, True)
#         count = count + 1
#         #count += 1
#         print(count)          
#     time.sleep(.1)
# GPIO.cleanup()
