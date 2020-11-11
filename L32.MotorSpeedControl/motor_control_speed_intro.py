''' The code demonstrates basic motor control
using functions to define motions such as
forward, backward, left_turn, right_turn, and stop.
'''
import time
import RPi.GPIO as GPIO

L_PWM = 36
R_PWM = 33
L_IN1 = 40
L_IN2 = 38
R_IN1 = 37
R_IN2 = 35

left_speed = None
right_speed = None

def init():
    global left_speed, right_speed

    print("Initializing the GPIO ports supporting drive ops.")
    #Configure GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    #set MC pins as output
    GPIO.setup(L_IN1, GPIO.OUT, initial = False)
    GPIO.setup(L_IN2, GPIO.OUT, initial = False)
    GPIO.setup(R_IN1, GPIO.OUT, initial = False)
    GPIO.setup(R_IN2, GPIO.OUT, initial = False)
  
    # set enable pins as output
    GPIO.setup(L_PWM, GPIO.OUT, initial = True)
    GPIO.setup(R_PWM, GPIO.OUT, initial = True)

    left_speed = GPIO.PWM(L_PWM, 50)
    right_speed = GPIO.PWM(R_PWM, 50)
    left_speed.start(0)
    right_speed.start(0)
  
def stop():
    
    # GPIO.output(L_IN1, False)
    # GPIO.output(L_IN2, False)
    # GPIO.output(R_IN1, False)
    # GPIO.output(R_IN2, False)
    left_speed.ChangeDutyCycle(0)
    right_speed.ChangeDutyCycle(0)


def forward(sec):
    print(f"Moving forward for {sec} seconds.")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, True)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, True)
    
    time.sleep(sec)
    stop()

def backward(sec):
    print(f"Moving backward for {sec} seconds.")
    GPIO.output(L_IN1, True)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, True)
    GPIO.output(R_IN2, False)
    
    time.sleep(sec)
    stop()

def right_turn(sec):
    #right turn by stop on right and forward on left
    print(f"Turning right for {sec} seconds.")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, True)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, False)
    
    time.sleep(sec)
    stop()

def left_turn(sec):
    #left turn by stop on left and forward on right
    print(f"Turning left for {sec} seconds.")
    GPIO.output(L_IN1, False)
    GPIO.output(L_IN2, False)
    GPIO.output(R_IN1, False)
    GPIO.output(R_IN2, True)
    
    time.sleep(sec)
    stop()

#program starts here
init()
left_speed.ChangeDutyCycle(50)
right_speed.ChangeDutyCycle(50)
forward(1)
time.sleep(1)   #be kind to the drive - full forward to full backward hurts!
backward(1)
time.sleep(1)   
left_turn(1)
time.sleep(1)   
right_turn(1)
time.sleep(1)
backward(1)
print("Done")
GPIO.cleanup()

