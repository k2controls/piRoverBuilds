''' piRover Bluetooth module
Provides interface to Yahboom smartphone
app enabling remote control of the piRover.
See next_action use in sample code at the bottom 
of this module.

Keith E. Kelly
v 1.2
4/2/21
'''
import time
from serial import Serial
from threading import Thread
from enum import Enum
from queue import SimpleQueue

class Action(Enum):
    STOP            = 0
    FORWARD         = 1
    BACKWARD        = 2
    LEFT            = 3
    RIGHT           = 4
    LEFT_ALT        = 5
    RIGHT_ALT       = 6

    BEEP            = 8
    SPEED_UP        = 9
    SPEED_DOWN      = 10
    SERVO_LEFT      = 11
    SERVO_MID       = 12
    SERVO_RIGHT     = 13
    LED_OFF         = 14
    LED_RED         = 15
    LED_GREEN       = 16
    LED_BLUE        = 18
    OUTFIRE         = 19
    LINE_FOLLOWER   = 20
    COLORFUL_SEARCH = 21
    OBSTACLE_AVOID  = 22
    GIMBAL_UP       = 23
    GIMBAL_DOWN     = 24
    GIMBAL_LEFT     = 25
    GIMBAL_RIGHT    = 26
    GIMBAL_CENTER   = 27

class ActionEvent(object):
    def __init__(self, action: Action):
        self.action = action
        self.time_stamp = time.time()

    def is_old(self):
        return self.time_stamp < time.time() - 1

    def __str__(self):
        return f"{self.action.name} occurred at {self.time_stamp}."
class Bluetooth(Thread):

    Messages = {
         "0,0,0,0,0,0,0,0,0": Action.STOP
        ,"1,0,0,0,0,0,0,0,0": Action.FORWARD
        ,"2,0,0,0,0,0,0,0,0": Action.BACKWARD
        ,"3,0,0,0,0,0,0,0,0": Action.LEFT
        ,"4,0,0,0,0,0,0,0,0": Action.RIGHT
        ,"0,1,0,0,0,0,0,0,0": Action.LEFT_ALT
        ,"0,2,0,0,0,0,0,0,0": Action.RIGHT_ALT
        ,"0,0,1,0,0,0,0,0,0": Action.BEEP
        ,"0,0,0,1,0,0,0,0,0": Action.SPEED_UP
        ,"0,0,0,2,0,0,0,0,0": Action.SPEED_DOWN
        ,"0,0,0,0,1,0,0,0,0": Action.SERVO_LEFT
        ,"0,0,0,0,2,0,0,0,0": Action.SERVO_RIGHT
        ,"0,0,0,0,0,0,1,0,0": Action.LED_OFF
        ,"0,0,0,0,0,0,2,0,0": Action.LED_RED
        ,"0,0,0,0,0,0,3,0,0": Action.LED_GREEN
        ,"0,0,0,0,0,0,4,0,0": Action.LED_BLUE
        ,"0,0,0,0,0,0,0,0,1": Action.SERVO_MID
        ,"0,0,0,0,0,0,0,1,0": Action.OUTFIRE
        ,"0,0,0,0,0,0,8,0,0": Action.LED_OFF
        ,"0,0,0,0,3,0,0,0,0": Action.GIMBAL_UP
        #,"0,0,0,0,3,8,0,0,0": Action.GIMBAL_DOWN
        # ,"0,0,0,0,0,8,0,0,0": Action.GIMBAL_LEFT
        # ,"0,0,0,0,0,8,0,0,0": Action.GIMBAL_RIGHT
        # ,"0,0,0,0,8,0,0,0,0": Action.GIMBAL_RELEASE
        ,"4WD,MODE21"       : Action.LINE_FOLLOWER
        ,"4WD,MODE31"       : Action.OBSTACLE_AVOID
        ,"4WD,MODE41"       : Action.COLORFUL_SEARCH
    }
  
    def __init__(self):
        self.serial = Serial("/dev/ttyAMA0", 9600)
        self.command_string = ""
        self.last_action = Action.STOP
        self.event_queue = SimpleQueue()
        Thread.__init__(self)
        self.daemon = True
        self.start()
    
    def run(self):
        while True:
            self.command_string = self._get_command_string()
            self.last_action = Bluetooth.Messages[self.command_string]
            action_event = ActionEvent(self.last_action)
            self.event_queue.put(action_event)    
            
    def _get_command_string(self):
        #wait for start
        cmd_str = ""
        while self.serial.read(1).decode() != "$":
            pass
        #wait for end
        while True:
            char = self.serial.read(1).decode()
            if char == "#":
                break
            cmd_str += char
        return cmd_str

    def next_action(self):
        action = None
        if not self.event_queue.empty():
            next_event = self.event_queue.get(block=False)
            if next_event.is_old():
                action = self.next_action()
            else:
                action = next_event.action
        return action

    def wait_for_action(self):
        action = None
        while action == None:
            action = self.next_action()
            time.sleep(.1)
        return action