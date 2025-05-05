import time
from machine import Pin, PWM

# Servo PWM frequency
SERVO_FREQ = 50  # Standard 50Hz for servos

# Pulse width range in microseconds
MIN_US = 544
MAX_US = 2400

# Full 16-bit range
FULL_DUTY = 65535


#initiallize button

#Initialize servo P

#joellle map
'''
PIN 0 AS 18 ON LHS TOP
10&13 == 23 & 34
16&14 == 1 & 25
17&15 == 36 & 32
11&9 == 33 & 30
18&NOFLAP = 0 & 24
NO Motor&12 = 35 & 31


'''

'''
# 1 - 36
# 7 - 34 

# 5 - 1
# 6 - 35

# 2 - 33

# 11 - 31
# 12 - 25

# 4 - 0

# 9 - 32

# 3 - 23
# 10 - 30

# not moving 

# 8 - 24 tried to move
'''


allPins = [23,0,1,36,33,35,24,25,32,30,31,34]

angles = {
    # pinNum: [closed, opens]
    23: [90, 170],
    0: [90, 170],
    1: [90, 180],  # DOESNT OPEN ALL THE WAY
    36: [60, 170], # BUZZES WHEN GPING BACK SOMETIMES????
    33: [90, 120], # BUZZES WHEN GPING BACK SOMETIMES????
    35: [90, 170],
    
    24: [0, 180],  # DOESNT OPEN ALL THE WAY
    25: [90, 170],
    32: [80, 140],
    30: [120, 180],    # DOESNT OPEN ALL THE WAY
    31: [70, 150],
    34: [120, 180]    # DOESNT OPEN ALL THE WAY
}

servos = []
print(angles.keys())
print('hi')
for k in allPins:
    SERVO_PIN6 = k  # Replace with your actual pin number
    servo_pwm6 = PWM(Pin(SERVO_PIN6))
    servo_pwm6.freq(SERVO_FREQ)
    servo_pwm6.duty_u16(0)    
    if k in angles.keys():
        print(k)
        print(type(k))
        print(angles[k])
        servos.append([k, servo_pwm6])


# Convert microseconds to duty_u16
def us_to_duty(us):
    # Period = 1 / 50Hz = 20ms = 20000us
    return int(FULL_DUTY * us / 20000)

# Move servo to a specific angle (0~180)
def set_servo_angle(servo_pwm, angle):
    if not 0 <= angle <= 180:
        raise ValueError("Angle must be between 0 and 180 degrees")
    pulsewidth = MIN_US + (MAX_US - MIN_US) * angle / 180
    duty = us_to_duty(pulsewidth)
    servo_pwm.duty_u16(duty)
    print(f"Moved servo to {angle} degrees (pulse {pulsewidth:.1f}us)")

# Manually stop the servo (optional)
def stop_servo(servo_pwm):
    servo_pwm.duty_u16(0)
    time.sleep(1)

start_a = 0
mid_a = 90
end_a = 130
blue_butt = Pin(38, Pin.IN, Pin.PULL_UP)

# Main demo loop
# AFTER BLUE BUTTON PRESSS: should close all vents, wait 2 secs, open all, wait, close
def main():
    PINS = [25]
    try:
        while True:
            if blue_butt.value() != 1:
                print('jijiji')
                
                for pin, serv in servos:
                    if pin in PINS:
                        print(pin)
                        set_servo_angle(serv, angles[pin][0])
                time.sleep(2)
                for pin, serv in servos:
                    if pin in PINS:
                        print(pin)
                        set_servo_angle(serv, angles[pin][1])
                
                time.sleep(2)
                for pin, serv in servos:
                    if pin in PINS:
                        print(pin)
                        set_servo_angle(serv, angles[pin][0])


    except KeyboardInterrupt:
        print("Stopping servo...")
        stop_servo(servo_pwm)

# # Execute
# if '__name__' == "__main__":
#     main()
main()