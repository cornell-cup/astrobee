import time
import sys
from .dc_motor import DCMotor

class DCMotorGroup(DCMotor):
    _DEFAULT_MOTOR_GROUP_INSTANCE = None

    @classmethod
    def get_default_motor_group(cls):
        """
        Get the default motor group instance. This is a singleton, so only one 
        instance of this motor group should exist at a time.  
        """
        if cls._DEFAULT_MOTOR_GROUP_INSTANCE is None:
            cls._DEFAULT_MOTOR_GROUP_INSTANCE = cls(
                DCMotor.get_default_motor(index=1),
                DCMotor.get_default_motor(index=2)
            )
        return cls._DEFAULT_MOTOR_GROUP_INSTANCE

    def __init__(self, *motors_param: DCMotor):
        """
        A wrapper class for multiple motors, allowing them to be treated as one motor.
        
        :param motors: The motors to add to this group
        :type motors: tuple<DCMotor>
        """
        self.motors = []
        for motor in motors_param:
            self.motors.append(motor)

    def set_group_throttle(self, throttle_percent: int):
        """
        :param throttle_percent: The throttle_percent to set all motors in this group to.
        :type throttle_percent: int
        """
        for motor in self.motors:
            motor.set_throttle(throttle_percent)
    
    def set_group_throttle_cycle(self, start_percent, end_percent, step, pause_time):
        """
        Ramp throttle in cycles, starting at start_percent, incrementing by step, and 
        ending at end_percent with pause_time between every throttle percent. 

        :param start_percent: starting throttle percent
        :type start_percent: int
        :param end_percent: ending throttle percent
        :type end_percent: int
        :param step: increment amount
        :type step: int
        :param pause_time: time to pause between setting throttle
        :type pause_time: int
        """
        try:
            self.calibrate_and_arm_group()

            for throttle in range(start_percent, end_percent + 1, step):
                self.set_group_throttle(throttle)
                time.sleep(pause_time)
                
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    key = sys.stdin.read(1)
                    if key.lower() == 's':
                        print("Detected 's' key. Stopping...")
                        raise KeyboardInterrupt
            
            for throttle in range(end_percent, start_percent - 1, -step):
                self.set_group_throttle(throttle)
                time.sleep(pause_time)
                
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    key = sys.stdin.read(1)
                    if key.lower() == 's':
                        print("Detected 's' key. Stopping...")
                        raise KeyboardInterrupt

        except KeyboardInterrupt:
            self.stop_group()
            print("program terminated by user.")

    def stop_group(self): 
        """
        Stop all the motors in the group. 
        """
        for motor in self.motors: 
            motor.stop()

    def calibrate_and_arm_group(self):
        """
        Individual calibrates each motor in the motor group. 
        ex. does the calibration for the first motor and then does the 
        calibration for the second motor. 
        """
        for motor in self.motors:
            motor.calibrate_and_arm()

if __name__ == "__main__":
    from XRPLib.defaults import *
    import select

    print("Press ENTER to start ESC calibration and throttle cycle...")
    input()

    motor_group.set_group_throttle_cycle(start_percent=20, end_percent=100, step=10, pause_time=2)