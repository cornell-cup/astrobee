from machine import Pin, PWM
import sys
import time
from XRPLib.pins import *

class Servo:
    _DEFAULT_SERVO_ONE_INSTANCE = None
    _DEFAULT_SERVO_TWO_INSTANCE = None
    _DEFAULT_SERVO_THREE_INSTANCE = None
    _DEFAULT_SERVO_FOUR_INSTANCE = None
    _DEFAULT_SERVO_FIVE_INSTANCE = None
    _DEFAULT_SERVO_SIX_INSTANCE = None
    _DEFAULT_SERVO_SEVEN_INSTANCE = None
    _DEFAULT_SERVO_EIGHT_INSTANCE = None
    _DEFAULT_SERVO_NINE_INSTANCE = None
    _DEFAULT_SERVO_TEN_INSTANCE = None
    _DEFAULT_SERVO_ELEVEN_INSTANCE = None
    _DEFAULT_SERVO_TWELVE_INSTANCE = None

    OPEN = 90
    CLOSE = 0

    @classmethod
    def get_default_servo(cls, index:int):
        """
        Gets one of the default XRP servo instances. These are singletons, so only one instance of each servo will ever exist.
        Raises an exception if an invalid index is requested.

        :param index: The index of the servo to get (1-12)
        :type index: int
        """
        if index == 1:
            if cls._DEFAULT_SERVO_ONE_INSTANCE is None:
                cls._DEFAULT_SERVO_ONE_INSTANCE = cls(SERVO_PIN1)
            servo = cls._DEFAULT_SERVO_ONE_INSTANCE
        elif index == 2:
            if cls._DEFAULT_SERVO_TWO_INSTANCE is None:
                cls._DEFAULT_SERVO_TWO_INSTANCE = cls(SERVO_PIN2)
            servo = cls._DEFAULT_SERVO_TWO_INSTANCE
        elif index == 3: 
            if cls._DEFAULT_SERVO_THREE_INSTANCE is None:
                cls._DEFAULT_SERVO_THREE_INSTANCE = cls(SERVO_PIN3)
            servo = cls._DEFAULT_SERVO_THREE_INSTANCE
        elif index == 4:
            if cls._DEFAULT_SERVO_FOUR_INSTANCE is None:
                cls._DEFAULT_SERVO_FOUR_INSTANCE = cls(SERVO_PIN4)
            servo = cls._DEFAULT_SERVO_FOUR_INSTANCE
        elif index == 5:
            if cls._DEFAULT_SERVO_FIVE_INSTANCE is None:
                cls._DEFAULT_SERVO_FIVE_INSTANCE = cls(SERVO_PIN5)
            servo = cls._DEFAULT_SERVO_FIVE_INSTANCE
        elif index == 6:
            if cls._DEFAULT_SERVO_SIX_INSTANCE is None:
                cls._DEFAULT_SERVO_SIX_INSTANCE = cls(SERVO_PIN6)
            servo = cls._DEFAULT_SERVO_SIX_INSTANCE
        elif index == 7:
            if cls._DEFAULT_SERVO_SEVEN_INSTANCE is None:
                cls._DEFAULT_SERVO_SEVEN_INSTANCE = cls(SERVO_PIN7)
            servo = cls._DEFAULT_SERVO_SEVEN_INSTANCE
        elif index == 8:
            if cls._DEFAULT_SERVO_EIGHT_INSTANCE is None:
                cls._DEFAULT_SERVO_EIGHT_INSTANCE = cls(SERVO_PIN8)
            servo = cls._DEFAULT_SERVO_EIGHT_INSTANCE
        elif index == 9:
            if cls._DEFAULT_SERVO_NINE_INSTANCE is None:
                cls._DEFAULT_SERVO_NINE_INSTANCE = cls(SERVO_PIN9)
            servo = cls._DEFAULT_SERVO_NINE_INSTANCE
        elif index == 10:
            if cls._DEFAULT_SERVO_TEN_INSTANCE is None:
                cls._DEFAULT_SERVO_TEN_INSTANCE = cls(SERVO_PIN10)
            servo = cls._DEFAULT_SERVO_TEN_INSTANCE
        elif index == 11:
            if cls._DEFAULT_SERVO_ELEVEN_INSTANCE is None:
                cls._DEFAULT_SERVO_ELEVEN_INSTANCE = cls(SERVO_PIN11)
            servo = cls._DEFAULT_SERVO_ELEVEN_INSTANCE
        elif index == 12:
            if cls._DEFAULT_SERVO_TWELVE_INSTANCE is None:
                cls._DEFAULT_SERVO_TWELVE_INSTANCE = cls(SERVO_PIN12)
            servo = cls._DEFAULT_SERVO_TWELVE_INSTANCE
        else:
            return Exception("Invalid servo index")
        return servo

    def __init__(self, signal_pin: int|str):
        """
        A simple class for interacting with a servo through PWM
        
        :param signal_pin: The pin the servo is connected to
        :type signal_pin: int | str
        """
        # Servo PWM frequency
        self.SERVO_FREQ = 50  # Standard 50Hz for servos

        # Pulse width range in microseconds
        self.MIN_US = 544
        self.MAX_US = 2400

        # Full 16-bit range
        self.FULL_DUTY = 65535

        self._servo = PWM(Pin(signal_pin))
        self._servo.freq(self.SERVO_FREQ)

    # Convert microseconds to duty_u16
    def us_to_duty(self, us):
        # Period = 1 / 50Hz = 20ms = 20000us
        return int(self.FULL_DUTY * us / 20000)

    # Move servo to a specific angle (0~180)
    def set_servo_angle(self, angle):
        """
        Sets the angle of the servo
        :param degrees: The angle to set the servo to [0,180]
        :ptype degrees: float
        """
        if not 0 <= angle <= 180:
            raise ValueError("Angle must be between 0 and 180 degrees")
        pulsewidth = self.MIN_US + (self.MAX_US - self.MIN_US) * angle / 180
        duty = self.us_to_duty(pulsewidth)
        self._servo.duty_u16(duty)
        # servo_pwm.duty_u16(duty)
        print(f"Moved servo to {angle} degrees (pulse {pulsewidth:.1f}us)")

    # Manually stop the servo (optional)
    def stop_servo(self):
        """
        Manually stop the servo
        """
        # servo_pwm.duty_u16(0)
        self._servo.duty_u16(0)
        time.sleep(1)