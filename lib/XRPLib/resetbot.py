import sys
"""
A simple file for shutting off all of the motors after a program gets interrupted from the REPL.
Run this file after interrupting a program to stop the robot by running "import XRPLib.resetbot" in the REPL.
"""

def reset_led():
    from XRPLib.board import Board
    # Turn off the on-board LED
    Board.get_default_board().led_off()
    try:
        # Turn off the RGB LED for boards that have it
        Board.get_default_board().set_rgb_led(0, 0, 0)
        # print("Reset board.")
    except:
        pass

def reset_servos():
    from XRPLib.servo import Servo
    # Turn off all Servos
    try:
        for i in range(12):
            Servo.get_default_servo(i+1).stop_servo()
            Servo.get_default_servo(i+1).close()
        # print("Reset servos.")
    except:
        pass

# def reset_hard():
#     reset_led()
#     reset_servos()
    
reset_servos()
reset_led()
print("Reset board and servos.")