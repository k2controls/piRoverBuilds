''' The code demonstrates basic motor control
using functions to define motions such as
forward, backward, left_turn, right_turn, and stop.
'''
import time

def init():
    print("Initializing the GPIO ports supporting drive ops.")
    
def forward(sec):
    print("Moving forward for " + str(sec) + " seconds.")
    time.sleep(sec)

def backward(sec):
    print("Moving backward for {} seconds.".format(sec))
    time.sleep(sec)

def right_turn(sec):
    print("Turning right for {} seconds.".format(sec))
    time.sleep(sec)

def left_turn(sec):
    print("Turning left for {} seconds.".format(sec))
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

