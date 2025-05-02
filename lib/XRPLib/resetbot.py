import sys
"""
A simple file for shutting off all of the motors after a program gets interrupted from the REPL.
Run this file after interrupting a program to stop the robot by running "import XRPLib.resetbot" in the REPL.
"""

def reset_motors():
    from XRPLib.dc_motor import DCMotor
    for i in range(2):
        motor = DCMotor.get_default_encoded_motor(i+1)
        motor.set_speed(0)
        
        # Double check if Astrobee has an encoder
        # motor.reset_encoder_position()

def reset_led():
    from XRPLib.board import Board
    # Turn off the on-board LED
    Board.get_default_board().led_off()
    try:
        # Turn off the RGB LED for boards that have it
        Board.get_default_board().set_rgb_led(0, 0, 0)
    except:
        pass

def reset_servos():
    from XRPLib.servo import Servo
    # Turn off all Servos
    for i in range(12):
        Servo.get_default_servo(i+1).free()

def reset_hard():
    reset_motors()
    reset_led()
    reset_servos()

# if "XRPLib.encoded_motor" in sys.modules:
#     reset_motors()

# if "XRPLib.board" in sys.modules:
#     reset_led()

# if "XRPLib.servo" in sys.modules:
#     reset_servos()