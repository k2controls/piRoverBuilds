''' Pushbutton Cycling LEDs using Counter
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

# Set pin Red LED as output, PB as input
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
# Set pushbutton pin as input
GPIO.setup(PB_PIN, GPIO.IN)

print("Press the pushbutton to cycle the LEDs through red, green, blue, and off.")

# Check the normal state of the push button
state = GPIO.input(PB_PIN)
print(f"Pushbutton is currently {state}.")

### i controls lED cycle - values 0 through 3
i = 0

while True:
    #wait for push
    while state == True:
        state = GPIO.input(PB_PIN)
    #wait for release
    while state == False:
        state = GPIO.input(PB_PIN)
    # Button has been push and then released. Increment i
    i = i + 1
    # i can only  be 0 through 3. Reset to zero if it goes to 4
    if i == 4:
        i = 0

    #update LEDs based on i value    
    if i == 0:
        #off
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, False)
    elif i == 1:
        #red
        GPIO.output(RED_PIN, True)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, False)
    elif i == 2:
        #green
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, True)
        GPIO.output(BLUE_PIN, False)
    elif i == 3:
        #blue
        GPIO.output(RED_PIN, False)
        GPIO.output(GREEN_PIN, False)
        GPIO.output(BLUE_PIN, True)

### i controls lED cycle - values 0 through 3
# i = 0
# cycle_counter = 0
# while cycle_counter < 5:

#     #update LEDs based on i value    
#     if i == 0:
#         #off
#         GPIO.output(RED_PIN, False)
#         GPIO.output(GREEN_PIN, False)
#         GPIO.output(BLUE_PIN, False)
#         cycle_counter = cycle_counter + 1
#         print(f"Cycled - count = {cycle_counter}")
#     elif i == 1:
#         #red
#         GPIO.output(RED_PIN, True)
#         GPIO.output(GREEN_PIN, False)
#         GPIO.output(BLUE_PIN, False)
#     elif i == 2:
#         #green
#         GPIO.output(RED_PIN, False)
#         GPIO.output(GREEN_PIN, True)
#         GPIO.output(BLUE_PIN, False)
#     elif i == 3:
#         #blue
#         GPIO.output(RED_PIN, False)
#         GPIO.output(GREEN_PIN, False)
#         GPIO.output(BLUE_PIN, True)

#     #wait for push
#     while GPIO.input(PB_PIN):
#         pass
#     #wait for release
#     while not GPIO.input(PB_PIN):
#         pass
#     # Button has been push and then released. Increment i
#     i = i + 1
#     # i can only  be 0 through 3. Reset to zero if it goes to 4
#     if i == 4:
#         i = 0
