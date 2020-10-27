''' The code demonstrates basic motor control
using functions to define motions such as
forward, backward, left_turn, right_turn, and stop.
'''
import time

def init():
    print("Initializing the GPIO ports supporting drive ops.")
    
def forward(sec):
    print(f"Moving forward for {sec} seconds.")
    time.sleep(sec)

def backward(sec):
    print(f"Moving backward for {sec} seconds.")
    time.sleep(sec)

def right_turn(sec):
    #right turn by stop on right and forward on left
    print(f"Turning right for {sec} seconds.")
    time.sleep(sec)

def left_turn(sec):
    #left turn by stop on left and forward on right
    print(f"Turning left for {sec} seconds.")
    time.sleep(sec)

#program starts here
init()
forward(4)
time.sleep(1)   #be kind to the drive - full forward to full backward hurts!
backward(4)
time.sleep(1)   
left_turn(2)
time.sleep(1)   
right_turn(4)
print("Done")

