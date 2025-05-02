from .pins import *
from .dc_motor_group import DCMotorGroup
from .servo import Servo
from .imu import IMU
import time
import math 

class YController:

    _DEFAULT_Y_CONTROLLER_INSTANCE = None

    @classmethod
    def get_default_y_controller(cls):
        """
        Get the default y controller instance. This is a singleton, so only one 
        instance should exist.
        """
        if cls._DEFAULT_Y_CONTROLLER_INSTANCE is None:
            cls._DEFAULT_Y_CONTROLLER_INSTANCE = cls(
                Servo.get_default_servo(3),
                Servo.get_default_servo(9),
                Servo.get_default_servo(1),
                Servo.get_default_servo(7),
                Servo.get_default_servo(2),
                Servo.get_default_servo(8),
                Servo.get_default_servo(4),
                Servo.get_default_servo(10), 
                IMU.get_default_imu()
            )
        return cls._DEFAULT_Y_CONTROLLER_INSTANCE

    def __init__(self, servo_three: Servo, servo_nine: Servo, servo_one: Servo, servo_seven: Servo, servo_two: Servo, servo_eight: Servo, servo_four: Servo, servo_ten: Servo, imu: IMU):
        """
        Y controller class for moving Astrobee along the y axis. 

        # TODO add docstring
        """
        # +y
        self.servo_three = servo_three
        self.servo_nine = servo_nine

        # -y
        self.servo_one = servo_one
        self.servo_seven = servo_seven

        # +Ry1
        self.servo_two = servo_two
        self.servo_eight = servo_eight

        # -Ry1
        self.servo_four = servo_four
        self.servo_ten = servo_ten

        self.imu = imu

    def move_pos_y(self, duration: int):
        """
        Move in +y direction. 

        :param duration: seconds to move in +y direction.
        :type duration: int
        """
        self.servo_three.set_servo_angle(Servo.OPEN)
        self.servo_nine.set_servo_angle(Servo.OPEN)

        time.sleep(duration)

        self.servo_three.set_servo_angle(Servo.CLOSE)
        self.servo_nine.set_servo_angle(Servo.CLOSE)

    def move_neg_y(self, duration: int): 
        """
        Move in -y direction.

        :param duration: seconds to move in =y direction.
        :type duration: int
        """        
        self.servo_one.set_servo_angle(Servo.OPEN)
        self.servo_seven.set_servo_angle(Servo.OPEN)

        time.sleep(duration)

        self.servo_one.set_servo_angle(Servo.CLOSE)
        self.servo_seven.set_servo_angle(Servo.CLOSE)

    def pos_rot_y(self, degree: int = None, duration: int = None):
        """
        Rotate about y axis with positive torque a specified degree. 

        :param degree: 
        :type degree: int
        :param duration: number of seconds to do turn if degree is not specified
        :type duration: int
        """

        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            else:
                self.servo_two.set_servo_angle(Servo.OPEN)
                self.servo_eight.set_servo_angle(Servo.OPEN)

                time.sleep(duration)

                self.servo_two.set_servo_angle(Servo.CLOSE)
                self.servo_eight.set_servo_angle(Servo.CLOSE)
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
            else:
                raise NotImplementedError
            
    def neg_rot_y(self, degree: int = None, duration: int = None):
        """
        Rotate about y axis with negative torque a specified degree. 

        :param degree: 
        :type degree: int
        :param duration: number of seconds to do turn if degree is not specified
        :type duration: int
        """

        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            else:
                self.servo_four.set_servo_angle(Servo.OPEN)
                self.servo_ten.set_servo_angle(Servo.OPEN)

                time.sleep(duration)

                self.servo_four.set_servo_angle(Servo.CLOSE)
                self.servo_ten.set_servo_angle(Servo.CLOSE)
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
            else:
                raise NotImplementedError