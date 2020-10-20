''' Line follower challenge/extension activity
Read line follower inputs and display status in terminal

Keith E. Kelly
10/20/20
'''
#import required libraries
import RPi.GPIO as GPIO
import time

#create constants to represent line follower pin numbers
LF_L2 = 5       # far left sensor
LF_L1 = 29      # near left sensor
LF_R1 = 7       # near right sensor
LF_R2 = 12      # far right sensor

# Configure GPIO setting
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Set LF pins as input
GPIO.setup(LF_L2, GPIO.IN)
GPIO.setup(LF_L1, GPIO.IN)
GPIO.setup(LF_R1, GPIO.IN)
GPIO.setup(LF_R2, GPIO.IN)

print("This solution indicates which line followers are 'hit'")
print()

while True:
    #use a variable and print
    state = GPIO.input(LF_L2)
    print(state)
    #just print the function
    print(GPIO.input(LF_L2))
    # add text
    #print("LF_L2 = " + state)
    print("LF_L2 = " + str(state))
    print("LF_L2 = {}".format(state))
    #use as if/else selection
    if state == True:
        print("LF_L2: searching for line...")
    else:
        print("LF_L2: line found!")
    time.sleep(1)

# import os
# while True:
#     if GPIO.input(LF_L2):
#         l2_sensor = "OFF"
#     else:
#         l2_sensor = " ON"
#     if GPIO.input(LF_L1):
#         l1_sensor = "OFF"
#     else:
#         l1_sensor = " ON"
#     if GPIO.input(LF_R1):
#         r1_sensor = "OFF"
#     else:
#         r1_sensor = " ON"
#     if GPIO.input(LF_R2):
#         r2_sensor = "OFF"
#     else:
#         r2_sensor = " ON"
        
#     os.system("clear")
#     print("LF_L2    LF_L1   LF_R1   LF_R2")
#     print("-------------------------------")
#     print(l2_sensor + "      " + l1_sensor + "      " + r1_sensor + "      " + r2_sensor)
#     # print(l2_sensor, end="      ")
#     # print(l1_sensor, end="      ")
#     # print(r1_sensor, end="      ")
#     # print(r2_sensor, end="      ")


