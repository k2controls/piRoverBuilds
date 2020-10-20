''' Line Follower Prep Solution
Preparation for later LF app than includes
piRover Drive.
Keith E. Kelly
10/16/20
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants to represent piRover LED pin numbers
RED_PIN = 15
GREEN_PIN = 13
BLUE_PIN = 18

#create constants to represent Line Follower pin numbers
# LF_L2     LF_L1   LF_R1   LF_R2
#   IN2     IN1     IN3     IN4
#   5       29      7       12

LF_L2 = 5
LF_L1 = 29
LF_R1 = 7
LF_R2 = 12


# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set specific pins as output
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
# Set specific pins as input
GPIO.setup(LF_L2, GPIO.IN)
GPIO.setup(LF_L1, GPIO.IN)
GPIO.setup(LF_R1, GPIO.IN)
GPIO.setup(LF_R2,GPIO.IN)
	
while True:
    l2 = GPIO.input(LF_L2)
    l1 = GPIO.input(LF_L1)
    r1 = GPIO.input(LF_R1)
    r2 = GPIO.input(LF_R2)

    if l2 and not l1 and not r1 and r2:
        print("Go")
    elif not l2 and l1 and r1 and r2:
        print("Hard Right")
    elif not l2 and not l1 and r1 and r2:
        print("Right")
    elif l2 and not l1 and r1 and r2:
        print("Right")
    elif l2 and l1 and r1 and not r2:
        print("Hard left")
    elif l2 and l1 and not r1 and not r2:
        print("Left")
    elif l2 and l1 and not r1 and r2:
        print("Left")
    elif l1 and l2 and r1 and r2:
        print("Stop")
    else:
        print("Invalid")
    time.sleep(.5)