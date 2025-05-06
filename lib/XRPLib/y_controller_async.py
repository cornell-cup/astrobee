import uasyncio as asyncio
from .pins import *
from .servo import Servo
import math

class YController:
    _DEFAULT_Y_CONTROLLER_INSTANCE = None
    @classmethod
    def get_default_y_controller(cls):
        """
        Get the default y controller instance. This is a singleton.
        """
        if cls._DEFAULT_Y_CONTROLLER_INSTANCE is None:
            cls._DEFAULT_Y_CONTROLLER_INSTANCE = cls(
                Servo.get_default_servo(11),
                Servo.get_default_servo(5),
                Servo.get_default_servo(12),
                Servo.get_default_servo(6)
            )
        return cls._DEFAULT_Y_CONTROLLER_INSTANCE
    # def __init__(self,
    #              servo_three: Servo,
    #              servo_nine:  Servo,
    #              servo_one:   Servo,
    #              servo_seven: Servo,
    #              servo_two:   Servo,
    #              servo_eight: Servo,
    #              servo_four:  Servo,
    #              servo_ten:   Servo):
    def __init__(self,
                 servo_eleven: Servo,
                 servo_five:  Servo,
                 servo_twelve:   Servo,
                 servo_six: Servo):
        """
        Y controller class for moving Astrobee along the y axis.
        """
        # +y
        # self.servo_three = servo_three
        # self.servo_nine  = servo_nine
        # # -y
        # self.servo_one    = servo_one
        # self.servo_seven = servo_seven
        # # +Ry1
        # self.servo_two   = servo_two
        # self.servo_eight = servo_eight
        # # -Ry1
        # self.servo_four  = servo_four
        # self.servo_ten   = servo_ten

        # # +Ry1
        self.servo_eleven = servo_eleven
        self.servo_five = servo_five
        # -Ry1
        self.servo_twelve  = servo_twelve
        self.servo_six   = servo_six

    # async def move_pos_y(self, duration: int):
    #     """
    #     Move in +y direction for a specified number of seconds.
    #     """
    #     self.servo_three.open()
    #     self.servo_nine.open()
    #     await asyncio.sleep(duration)
    #     self.servo_three.close()
    #     self.servo_nine.close()
    # async def move_neg_y(self, duration: int):
    #     """
    #     Move in -y direction for a specified number of seconds.
    #     """
    #     self.servo_one.open()
    #     self.servo_seven.open()
    #     await asyncio.sleep(duration)
    #     self.servo_one.close()
    #     self.servo_seven.close()
    async def pos_rot_y(self, degree: int = None, duration: int = None):
        """
        Rotate about y axis with positive torque.
        If `degree` is provided, raises NotImplementedError.
        Otherwise uses `duration` in seconds.
        """
        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            self.servo_eleven.open()
            self.servo_five.open()
            await asyncio.sleep(duration)
            self.servo_eleven.close()
            self.servo_five.close()
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
                return
            raise NotImplementedError("Degree-based rotation not yet implemented")
    
    async def neg_rot_y(self, degree: int = None, duration: int = None):
        """
        Rotate about y axis with negative torque.
        If `degree` is provided, raises NotImplementedError.
        Otherwise uses `duration` in seconds.
        """
        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            self.servo_twelve.open()
            self.servo_six.open()
            await asyncio.sleep(duration)
            self.servo_twelve.close()
            self.servo_six.close()
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
                return
            raise NotImplementedError("Degree-based rotation not yet implemented")