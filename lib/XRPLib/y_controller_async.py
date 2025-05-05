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
                Servo.get_default_servo(3),
                Servo.get_default_servo(9),
                Servo.get_default_servo(1),
                Servo.get_default_servo(7),
                Servo.get_default_servo(2),
                Servo.get_default_servo(8),
                Servo.get_default_servo(4),
                Servo.get_default_servo(10),
            )
        return cls._DEFAULT_Y_CONTROLLER_INSTANCE
    def __init__(self,
                 servo_three: Servo,
                 servo_nine:  Servo,
                 servo_one:   Servo,
                 servo_seven: Servo,
                 servo_two:   Servo,
                 servo_eight: Servo,
                 servo_four:  Servo,
                 servo_ten:   Servo):
        """
        Y controller class for moving Astrobee along the y axis.
        """
        # +y
        self.servo_three = servo_three
        self.servo_nine  = servo_nine
        # -y
        self.servo_one    = servo_one
        self.servo_seven = servo_seven
        # +Ry1
        self.servo_two   = servo_two
        self.servo_eight = servo_eight
        # -Ry1
        self.servo_four  = servo_four
        self.servo_ten   = servo_ten
    async def move_pos_y(self, duration: int):
        """
        Move in +y direction for a specified number of seconds.
        """
        self.servo_three.open()
        self.servo_nine.open()
        await asyncio.sleep(duration)
        self.servo_three.close()
        self.servo_nine.close()
    async def move_neg_y(self, duration: int):
        """
        Move in -y direction for a specified number of seconds.
        """
        self.servo_one.open()
        self.servo_seven.open()
        await asyncio.sleep(duration)
        self.servo_one.close()
        self.servo_seven.close()
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
            self.servo_two.open()
            self.servo_eight.open()
            await asyncio.sleep(duration)
            self.servo_two.close()
            self.servo_eight.close()
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
            self.servo_four.open()
            self.servo_ten.open()
            await asyncio.sleep(duration)
            self.servo_four.close()
            self.servo_ten.close()
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
                return
            raise NotImplementedError("Degree-based rotation not yet implemented")