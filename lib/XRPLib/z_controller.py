from .servo import Servo
from .imu import IMU
import time
import math 

class ZController:

    _DEFAULT_Z_CONTROLLER_INSTANCE = None

    @classmethod
    def get_default_z_controller(cls):
        """
        Get the default z controller instance. This is a singleton, so only one 
        instance should exist.
        """
        if cls._DEFAULT_Z_CONTROLLER_INSTANCE is None:
            cls._DEFAULT_Z_CONTROLLER_INSTANCE = cls(
                Servo.get_default_servo(4),
                Servo.get_default_servo(8),
                Servo.get_default_servo(2),
                Servo.get_default_servo(10),
                Servo.get_default_servo(3),
                Servo.get_default_servo(7),
                Servo.get_default_servo(1),
                Servo.get_default_servo(9)            
            )
        return cls._DEFAULT_Z_CONTROLLER_INSTANCE

    def __init__(self, servo_four: Servo, servo_eight: Servo, servo_two: Servo, servo_ten: Servo, servo_three: Servo, servo_seven: Servo, servo_one: Servo, servo_nine: Servo):
        """
        Z controller class for moving Astrobee along the z axis. 

        TODO finish docstring
        """

        # +z
        self.servo_four = servo_four
        self.servo_eight = servo_eight

        # -z
        self.servo_two = servo_two
        self.servo_ten = servo_ten

        # +Rz1
        self.servo_three = servo_three
        self.servo_seven = servo_seven

        # -Rz1
        self.servo_one = servo_one
        self.servo_nine = servo_nine

    def move_pos_z(self, duration: int):
        """
        Move in +z direction. 

        :param duration: seconds to move in +z direction.
        :type duration: int
        """        
        self.servo_four.open()
        self.servo_eight.open()

        time.sleep(duration)

        self.servo_four.close()
        self.servo_eight.close()


    def move_neg_z(self, duration: int): 
        """
        Move in -z direction. 

        :param duration: seconds to move in -z direction.
        :type duration: int
        """
        self.servo_two.open()
        self.servo_ten.open()

        time.sleep(duration)

        self.servo_two.close()
        self.servo_ten.close()

    def pos_rot_z(self, degree: int = None, duration: int = None):
        """
        Rotate about z axis with positive torque a specified degree. 

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
                self.servo_three.open()
                self.servo_seven.open()

                time.sleep(duration)

                self.servo_three.close()
                self.servo_seven.close()
        elif degree is not None:
            if duration is not None:
                print("Degree and duration cannot both be specified")
            else:
                raise NotImplementedError
            
    def neg_rot_z(self, degree: int = None, duration: int = None):
        """
        Rotate about z axis with negative torque a specified degree. 

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
                self.servo_one.open()
                self.servo_nine.open()

                time.sleep(duration)

                self.servo_one.close()
                self.servo_nine.close()
        elif degree is not None:
            if duration is not None:
                print("Degree and duration cannot both be specified")
            else:
                raise NotImplementedError
