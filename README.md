Use the straight() and turn() methods in lib/XRPLib/differential_drive.py as reference for implementing the methods in the controller files (x_controller.py, etc.)

All the hardware is defined in lib/XRPLib/defaults.py which is imported at the top
of every controller file. So just call dc_motor_group.method() or servo_one.set_servo_angle() to use them. 