import uasyncio as asyncio
from .pins import *
from .servo import Servo

import math

class XController:
    _DEFAULT_X_CONTROLLER_INSTANCE = None
    
    @classmethod
    def get_default_x_controller(cls):
        """
        Get the default x controller instance. This is a singleton.
        """
        if cls._DEFAULT_X_CONTROLLER_INSTANCE is None:
            cls._DEFAULT_X_CONTROLLER_INSTANCE = cls(
                Servo.get_default_servo(11),
                Servo.get_default_servo(12),
                Servo.get_default_servo(5),
                Servo.get_default_servo(6),
                Servo.get_default_servo(1),
                Servo.get_default_servo(3),
                Servo.get_default_servo(2),
                Servo.get_default_servo(4),
            )
        return cls._DEFAULT_X_CONTROLLER_INSTANCE
    def __init__(self,
                 servo_eleven: Servo,
                 servo_twelve:  Servo,
                 servo_five:    Servo,
                 servo_six:     Servo,
                 servo_one:     Servo,
                 servo_three:   Servo,
                 servo_two:     Servo,
                 servo_four:    Servo):
        """
        X controller class for moving Astrobee along the x axis.
        """
        # +x
        self.servo_eleven = servo_eleven
        self.servo_twelve = servo_twelve
        # -x
        self.servo_five    = servo_five
        self.servo_six     = servo_six
        # +Rx1
        self.servo_one     = servo_one
        self.servo_three   = servo_three
        # -Rx1
        self.servo_two     = servo_two
        self.servo_four    = servo_four
        
    async def move_pos_x(self, duration: int):
        """
        Move in +x direction for a specified number of seconds.
        """
        self.servo_eleven.open()
        self.servo_twelve.open()
        await asyncio.sleep(duration)
        self.servo_eleven.close()
        self.servo_twelve.close()
        
    async def move_neg_x(self, duration: int):
        """
        Move in -x direction for a specified number of seconds.
        """
        self.servo_five.open()
        self.servo_six.open()
        
        await asyncio.sleep(duration)
        
        self.servo_five.close()
        self.servo_six.close()
        
    async def pos_rot_x(self, degree: int = None, duration: int = None):
        """
        Rotate about x axis with positive torque.
        If `degree` is provided, raises NotImplementedError.
        Otherwise uses `duration` in seconds.
        """
        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            self.servo_one.open()
            self.servo_three.open()
            await asyncio.sleep(duration)
            self.servo_one.close()
            self.servo_three.close()
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
                return
            raise NotImplementedError("Degree-based rotation not yet implemented")
    async def neg_rot_x(self, degree: int = None, duration: int = None):
        """
        Rotate about x axis with negative torque.
        If `degree` is provided, raises NotImplementedError.
        Otherwise uses `duration` in seconds.
        """
        if degree is None:
            if duration is None:
                print("Either degree or duration needs to be specified.")
                return
            self.servo_two.open()
            self.servo_four.open()
            await asyncio.sleep(duration)
            self.servo_two.close()
            self.servo_four.close()
        else:
            if duration is not None:
                print("Degree and duration cannot both be specified")
                return
            raise NotImplementedError("Degree-based rotation not yet implemented")