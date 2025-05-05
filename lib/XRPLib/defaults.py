from .board import Board
# from .imu import IMU
from .servo import Servo
from .x_controller_async import XController
from .y_controller_async import YController
from .z_controller_async import ZController

"""
A simple file that constructs all of the default objects for the XRP robot
Run "from XRPLib.defaults import *" to use
"""
board = Board.get_default_board()

# imu = IMU.get_default_imu()

servo_one = Servo.get_default_servo(index=1)
servo_two = Servo.get_default_servo(index=2)
servo_three = Servo.get_default_servo(index=3)
servo_four = Servo.get_default_servo(index=4)
servo_five = Servo.get_default_servo(index=5)
servo_six = Servo.get_default_servo(index=6)
servo_seven = Servo.get_default_servo(index=7)
servo_eight = Servo.get_default_servo(index=8)
servo_nine = Servo.get_default_servo(index=9)
servo_ten = Servo.get_default_servo(index=10)
servo_eleven = Servo.get_default_servo(index=11)
servo_twelve = Servo.get_default_servo(index=12)

x_controller = XController.get_default_x_controller()
y_controller = YController.get_default_y_controller()
z_controller = ZController.get_default_z_controller()