''' Keyboard Drive Solution
This solution accepts an input from the user's
phone connected to the piRover via Bluetooth.
See prior lessons on connecting to Bluetooth.

Keith E. Kelly
11/19/20
'''
# from piRover_commands import *
from piRover_drive import *
from piRover_bluetooth import Bluetooth, Action

def do_action(action):
    if action == Action.FORWARD:
        #print("you are going forward...")
        forward()
    elif action == Action.BACKWARD:
        #print("you are going backward...")
        backward()
    elif action == Action.LEFT:
        #print("you are turning left forward...")
        left_forward()
    elif action == Action.LEFT_ALT:
        #print("you are rotating left...")
        left_rotate()        
    elif action == Action.RIGHT:
        #print("you are turning right forward...")
        right_forward()
    elif action == Action.RIGHT_ALT:
        #print("you are rotating right...")
        right_rotate()
    elif action == Action.STOP:
        #print("you are stopped.")    
        stop()
    elif action == Action.SPEED_UP:
        #print("you are accelerating...")
        accelerate()    
    elif action == Action.SPEED_DOWN:
        #print("you are decelerating...")
        decelerate()

def main():
    drive_init()
    bt = Bluetooth()
    print("Welcome to Bluetooth Drive")
    print()
    print("Connect your Bluetooth device to drive the piRover!")
    last_action = None
    while True:
        action = bt.wait_for_action()
        print(action.name)
        do_action(action)
        if last_action == Action.LED_OFF and action == Action.LED_OFF:
            print("Quit? Press LED off again to quit.")
            if bt.next_action() == Action.LED_OFF:
                break
        last_action = action

    print("Done")

if __name__ == "__main__":
    main()
