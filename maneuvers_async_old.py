from lib.XRPLib.defaults import *
import uasyncio as asyncio
import random


DURATION_1 = 1  # seconds for each move/rotate
DURATION_2 = 2  # seconds for each move/rotate
DURATION_3 = 3  # seconds for each move/rotate


# State
maneuver_names = [
    "M1: Z-Trans 1s",  "M2: X-Trans 1s",  "M3: Y-Trans 1s",
    "M4: X-Rot 1s",    "M5: Y-Rot 1s",    "M6: Z-Rot 1s",
    "M7: Z-Trans 2s",  "M8: X-Trans 2s",  "M9: Y-Trans 2s",
    "M10: X-Rot 2s",   "M11: Y-Rot 2s",   "M12: Z-Rot 2s",
    "M13: Z-Trans 3s", "M14: X-Trans 3s", "M15: Y-Trans 3s",
    "M16: X-Rot 3s",   "M17: Y-Rot 3s",   "M18: Z-Rot 3s",
    "M19: X Spin 3s",  "M20: Y Spin 3s",  "M21: Z Spin 3s"
]
full_emotions = [
    "neutral", "sick", "vomit", "vomit2", "ready_to_race", "sad", "idle_stable", 
    "startled", "yes", "love_it", "chuckle", "blink_awake", "surprise"
]
emotions = full_emotions.copy()
index = 0
started = False
maneuver_task = None

# Helpers
async def off_the_ground(duration_seconds):
    await y_controller.move_pos_y(duration_seconds)
    
async def on_ground(duration_seconds):
    await y_controller.move_neg_y(duration_seconds)
    
def stop_everything():
    for i in range(12):
        s = Servo.get_default_servo(i+1)
        s.stop_servo()
        s.close()
        
def play_random_emotion():
    global emotions, full_emotions
    if len(emotions) == 0:
        emotions = full_emotions.copy()
    random_int = random.randint(0, len(emotions)-1)  # inclusive of both 0 and len(emotions)-1
    emotion_playing = emotions[random_int]
    print(f"SPR,{emotion_playing}")
    emotions.pop(random_int)
    
# Maneuvers
async def maneuver_1():
    try:
        await off_the_ground(DURATION_1)
        play_random_emotion()
        await z_controller.move_pos_z(DURATION_1)
        await z_controller.move_neg_z(DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_2():
    try:
        await off_the_ground(DURATION_1)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await x_controller.move_neg_x(DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_3():
    try:
        await off_the_ground(DURATION_1)
        await y_controller.move_pos_y(DURATION_1)
        await y_controller.move_neg_y(DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_4():
    try:
        await off_the_ground(DURATION_1)
        await x_controller.pos_rot_x(duration=DURATION_1)
        await x_controller.neg_rot_x(duration=DURATION_1)
        await x_controller.pos_rot_x(duration=DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_5():
    try:
        await off_the_ground(DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
        await y_controller.neg_rot_y(duration=DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_6():
    try:
        await off_the_ground(DURATION_1)
        await z_controller.pos_rot_z(duration=DURATION_1)
        await z_controller.neg_rot_z(duration=DURATION_1)
        await z_controller.pos_rot_z(duration=DURATION_1)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_7():
    try:
        await off_the_ground(DURATION_2)
        play_random_emotion()
        await z_controller.move_pos_z(DURATION_2)
        await z_controller.move_neg_z(DURATION_2)
        await on_ground(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_8():
    try:
        await off_the_ground(DURATION_2)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await x_controller.move_neg_x(DURATION_2)
        await on_ground(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_9():
    try:
        await off_the_ground(DURATION_2)
        await y_controller.move_pos_y(DURATION_2)
        await y_controller.move_neg_y(DURATION_2)
        await on_ground(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_10():
    try:
        await off_the_ground(DURATION_2)
        await x_controller.pos_rot_x(duration=DURATION_2)
        await x_controller.neg_rot_x(duration=DURATION_2)
        await x_controller.pos_rot_x(duration=DURATION_2)
        await on_ground(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_11():
    try:
        await off_the_ground(DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
        await y_controller.neg_rot_y(duration=DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
        await on_ground(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_12():
    try:
        await off_the_ground(DURATION_2)
        await z_controller.pos_rot_z(duration=DURATION_2)
        await z_controller.neg_rot_z(duration=DURATION_2)
        await z_controller.pos_rot_z(duration=DURATION_2)
        await on_ground()
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_13():
    try:
        await off_the_ground(DURATION_3)
        play_random_emotion()
        await z_controller.move_pos_z(DURATION_3)
        await z_controller.move_neg_z(DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_14():
    try:
        await off_the_ground(DURATION_3)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await x_controller.move_neg_x(DURATION_1)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_15():
    try:
        await off_the_ground(DURATION_3)
        await y_controller.move_pos_y(DURATION_3)
        await y_controller.move_neg_y(DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_16():
    try:
        await off_the_ground(DURATION_3)
        await x_controller.pos_rot_x(duration=DURATION_3)
        await x_controller.neg_rot_x(duration=DURATION_3)
        await x_controller.pos_rot_x(duration=DURATION_3)
        await on_ground(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_17():
    try:
        await off_the_ground(DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.neg_rot_y(duration=DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_18():
    try:
        await off_the_ground(DURATION_3)
        await z_controller.pos_rot_z(duration=DURATION_3)
        await z_controller.neg_rot_z(duration=DURATION_3)
        await z_controller.pos_rot_z(duration=DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_19():
    try:
        await off_the_ground(DURATION_3)
        await x_controller.pos_rot_x(duration=DURATION_3)
        await x_controller.pos_rot_x(duration=DURATION_3)
        await x_controller.pos_rot_x(duration=DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_20():
    try:
        await off_the_ground(DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_21():
    try:
        await off_the_ground(DURATION_3)
        await z_controller.pos_rot_z(duration=DURATION_3)
        await z_controller.pos_rot_z(duration=DURATION_3)
        await z_controller.pos_rot_z(duration=DURATION_3)
        await on_ground(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
# Button Handler
async def button_handler():
    global index, started, maneuver_task
    
    setup = False
    while setup is False:
        print("ASK,Connected.")
        await asyncio.sleep_ms(200)
        if board.is_select_pressed():
            setup = True
    print(f"ASK,{maneuver_names[index]}")
    while True:
        await asyncio.sleep_ms(50)
        # Cycle through maneuvers
        if board.is_select_pressed() and not started:
            await asyncio.sleep_ms(200)
            if board.is_select_pressed():
                index = (index + 1) % len(maneuver_names)
                print(f"ASK,{maneuver_names[index]}")
            while board.is_select_pressed():
                await asyncio.sleep_ms(20)
        # Start/Stop the current maneuver
        if board.is_start_stop_pressed():
            await asyncio.sleep_ms(200)
            if board.is_start_stop_pressed():
                if started:
                    print(f"ASK,Stopped M{index+1}")
                    started = False
                    if maneuver_task:
                        maneuver_task.cancel()
                        maneuver_task = None
                    stop_everything()
                else:
                    print(f"ASK,Started M{index+1}")
                    started = True
                    await asyncio.sleep(1)  # let the print flush
                    coro = globals()[f"maneuver_{index+1}"]
                    maneuver_task = asyncio.create_task(coro())
            while board.is_start_stop_pressed():
                await asyncio.sleep_ms(20)
# Main Entrypoint
async def main():
    asyncio.create_task(button_handler())
    while True:
        await asyncio.sleep(1)
        
# Run!
asyncio.run(main())