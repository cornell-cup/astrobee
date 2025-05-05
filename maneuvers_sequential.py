from lib.XRPLib.defaults import *
import time
import random

DURATION = 2   

# Getting off of the ground
def off_the_ground():
    y_controller.move_pos_y(DURATION)

# Getting back to the ground
def on_ground():
    y_controller.move_neg_y(DURATION)

def stop_everything():
    for i in range(12):
        Servo.get_default_servo(i+1).stop_servo()
        Servo.get_default_servo(i+1).close()
    
## Maneuvers ##
# 1: Move forward, stop, and move backward along the z axis
def maneuver_1():
    global started
    
    # while name is displayed, rise from ground and stop
    off_the_ground()
    
    # play the emotion after leaving the ground
    play_random_emotion()

    # go forward along z axis and stop
    z_controller.move_pos_z(DURATION)

    # go backward along z axis and stop
    z_controller.move_neg_z(DURATION)

    # go back to ground
    on_ground()

    # indicate that the maneuver
    started = False
    

# 2. Move forward, stop, and move backward along the x axis
def maneuver_2():
    global started
    
    # while name is displayed, rise from ground and stop
    off_the_ground()
    
    # play the emotion after leaving the ground
    play_random_emotion()

    # go forward along x axis and stop
    x_controller.move_pos_x(DURATION)

    # go backward along x axis and stop
    x_controller.move_neg_x(DURATION)

    # go back to ground
    on_ground()
    
    # # indicate that the maneuver
    # started = False

# 3. Move forward, stop, and move backward along the y axis
def maneuver_3():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # go forward along y axis and stop
    y_controller.move_pos_y(DURATION)

    # go backward along y axis and stop
    y_controller.move_neg_y(DURATION)

    # go back to ground
    on_ground()

# 4. Rotate 90 degrees, stop, and rotate back 180 degrees along the x axis, stop, rotate 90 degrees back to center
def maneuver_4():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along x axis and stop
    x_controller.pos_rot_x(duration=DURATION)
    
    # rotate -180 degrees along x axis and stop
    x_controller.neg_rot_x(duration=DURATION)
    
    # rotate +90 degrees aong x axis back to original position
    x_controller.pos_rot_x(duration=DURATION)

    # go back to ground
    on_ground()


# 5. Rotate 90 degrees, stop, and rotate back 180 degrees along the y axis, stop, rotate 90 degrees back to center
def maneuver_5():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along y axis and stop
    y_controller.pos_rot_y(duration=DURATION)
    
    # rotate -180 degrees along y axis and stop
    y_controller.neg_rot_y(duration=DURATION)
    
    # rotate +90 degrees aong y axis back to original position
    y_controller.pos_rot_y(duration=DURATION)

    # go back to ground
    on_ground()


# 6. Rotate 90 degrees, stop, and rotate back 180 degrees along the z axis, stop, rotate 90 degrees back to center
def maneuver_6():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along z axis and stop
    z_controller.pos_rot_z(duration=DURATION)
    
    # rotate -180 degrees along z axis and stop
    z_controller.neg_rot_z(duration=DURATION)
    
    # rotate +90 degrees along z axis back to original position
    z_controller.pos_rot_z(duration=DURATION)

    # go back to ground
    on_ground()

# 7: CLOSED LOOP Move forward, stop, and move backward along the z axis
def maneuver_7():
     # while name is displayed, rise from ground and stop
    off_the_ground()

    # go forward along z axis and stop
    z_controller.move_pos_z(DURATION)

    # go backward along z axis and stop
    z_controller.move_neg_z(DURATION)

    # go back to ground
    on_ground()

# 8. CLOSED LOOP Move forward, stop, and move backward along the x axis
def maneuver_8():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # go forward along x axis and stop
    x_controller.move_pos_x(DURATION)

    # go backward along x axis and stop
    x_controller.move_neg_x(DURATION)

    # go back to ground
    on_ground()

# 9. CLOSED LOOP Move forward, stop, and move backward along the y axis
def maneuver_9():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # go forward along y axis and stop
    y_controller.move_pos_y(DURATION)

    # go backward along y axis and stop
    y_controller.move_neg_y(DURATION)

    # go back to ground
    on_ground()

# 10. CLOSED LOOP Rotate 90 degrees, stop, and rotate back 180 degrees along the x axis, stop, rotate 90 degrees back to center
def maneuver_10():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along x axis and stop
    x_controller.pos_rot_x(degree=90)
    
    # rotate -180 degrees along x axis and stop
    x_controller.neg_rot_x(degree=180)
    
    # rotate +90 degrees aong x axis back to original position
    x_controller.pos_rot_x(degree=90)

    # go back to ground
    on_ground()


# 11. CLOSED LOOP Rotate 90 degrees, stop, and rotate back 180 degrees along the y axis, stop, rotate 90 degrees back to center
def maneuver_11():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along y axis and stop
    y_controller.pos_rot_y(degree=90)
    
    # rotate -180 degrees along y axis and stop
    y_controller.neg_rot_y(degree=180)
    
    # rotate +90 degrees aong y axis back to original position
    y_controller.pos_rot_y(degree=90)

    # go back to ground
    on_ground()


# 12. CLOSED LOOP Rotate 90 degrees, stop, and rotate back 180 degrees along the z axis, stop, rotate 90 degrees back to center
def maneuver_12():
    # while name is displayed, rise from ground and stop
    off_the_ground()

    # rotate +90 degrees along z axis and stop
    z_controller.pos_rot_z(degree=90)
    
    # rotate -180 degrees along z axis and stop
    z_controller.neg_rot_z(degree=180)
    
    # rotate +90 degrees along z axis back to original position
    z_controller.pos_rot_z(degree=90)

    # go back to ground
    on_ground()

def test():
    global started
    print("Test")
    time.sleep(1)
    play_random_emotion()
    started = False
    
def play_random_emotion():
    global emotions, full_emotions
    if len(emotions) == 0:
        emotions = full_emotions.copy()
    random_int = random.randint(0, len(emotions)-1)  # inclusive of both 0 and len(emotions)-1
    emotion_playing = emotions[random_int]
    print(f"SPR,{emotion_playing}")
    emotions.pop(random_int)

maneuver_names = ["M1: Z-Trans OL", "M2: X-Trans OL", "M3: Y-Trans OL", "M4: X-Rot OL", "M5: Y-Rot OL", "M6: Z-Rot OL", "M7: Z-Trans CL", "M8: X-Trans CL", "M9: Y-Trans CL", "M10: X-Rot CL", "M11: Y-Rot CL", "M12: Z-Rot CL"]
full_emotions = ["startled", "big_yes", "big_no", "surprise2", "neutral", "happy2", "love_it", "ready_to_race", "vomit", "chuckle", "excited", "blink_awake"]
emotions = full_emotions.copy()

index = 0
started = False
chosen_maneuver = None
print(f"ASK,{maneuver_names[0]}")

while True:
    if board.is_select_pressed() is True and started is False:
        time.sleep(1)
        
        index = index + 1
        index = index % len(maneuver_names)
        chosen_maneuver = maneuver_names[index]
        print(f"ASK,{chosen_maneuver}")
    elif board.is_start_stop_pressed() is True:
        # STOP a maneuver
        if started is True: 
            print(f"ASK,Stopped M{index+1}")
            started = False
            time.sleep(1)
            stop_everything()
            
        # START a maneuver
        elif started is False:
            print(f"ASK,Started M{index+1}")
            time.sleep(1)
            started = True
            
            method_name = f"maneuver_{index+1}"
            
            if method_name == "maneuver_1":
                globals()[method_name]()