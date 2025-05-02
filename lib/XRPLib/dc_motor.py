import time
from machine import Pin, PWM
import sys
from XRPLib.pins import *

class DCMotor:
    _DEFAULT_MOTOR_ONE_INSTANCE = None
    _DEFAULT_MOTOR_TWO_INSTANCE = None

    @classmethod
    def get_default_motor(cls, index: int):
        """
        Gets one of the two motor instances. These are singletons, so only one
        instance of each motor will ever exist. 

        Raises an exception if an invalid index is requested. 

        :param index: The index of the motor to get (1, 2)
        :type index: int
        """

        if index == 1:
            if cls._DEFAULT_MOTOR_ONE_INSTANCE is None:
                cls._DEFAULT_MOTOR_ONE_INSTANCE = cls(ESC_PIN_1)
            motor = cls._DEFAULT_MOTOR_ONE_INSTANCE
        elif index == 2:
            if cls._DEFAULT_MOTOR_TWO_INSTANCE is None:
                cls._DEFAULT_MOTOR_TWO_INSTANCE = cls(ESC_PIN_2)
            motor = cls._DEFAULT_MOTOR_TWO_INSTANCE
        else:
            return Exception("Invalid motor index.")
        return motor
    
    def __init__(self, signal_pin: int):
        self._motor = PWM(Pin(signal_pin))
        self._motor.freq(50)

        # Define min and max duty cycle for ESCs
        self.MIN_DUTY = int(65535 * 1 / 20)  # 1ms pulse (5% duty cycle)
        self.MAX_DUTY = int(65535 * 2 / 20)  # 2ms pulse (10% duty cycle)

    def set_throttle(self, throttle_percent):
        """
        Set the throttle for one dc motor.

        :param throttle_percent:
        :type throttle_percent: int
        """
        duty_value = int(self.MIN_DUTY + (throttle_percent / 100) * (self.MAX_DUTY- self.MIN_DUTY))
        self._motor.duty_u16(duty_value)
        print(f"Throttle set to {throttle_percent}%")
    
    def stop(self):
        """
        Stop the dc motor. 
        """
        print("Stopping motors...")
        self._motor.duty_u16(self.MIN_DUTY)
        time.sleep(1)
        self._motor.deinit()  # Deinitialize PWM properly
        print("Motors stopped and PWM released.\n")

    def calibrate_and_arm(self):
        print("calibrating ESCs")
        
        self._motor.duty_u16(0)
        time.sleep(0.5)

        self._motor.duty_u16(self.MAX_DUTY)
        time.sleep(2)

        self._motor.duty_u16(self.MIN_DUTY)
        time.sleep(2)

        print("ESC calibration complete. Arming ESC...")
        self._motor.duty_u16(self.MIN_DUTY)
        time.sleep(3)
        print("ESC armed.\n")
