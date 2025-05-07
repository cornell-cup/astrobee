from lib.XRPLib.defaults import *
import uasyncio as asyncio
import random


DURATION_1 = 1  # seconds for each move/rotate
DURATION_2 = 2  # seconds for each move/rotate
DURATION_3 = 3  # seconds for each move/rotate


# State
maneuver_names = [
    "M1: X-Trans 1s",  "M2: Y-Rot 1s",  "M3: X-T,Y-R 1s", "M4: X-T,Y-R,X-T 1s",
    "M5: X-Trans 2s",  "M6: Y-Rot 2s",  "M7: X-T,Y-R 2s", "M8: X-T,Y-R,X-T 2s",
    "M9: X-Trans 3s",  "M10: Y-Rot 3s", "M11: X-T,Y-R 3s","M12: X-T,Y-R,X-T 3s",
    "M13: RTRT 1s", "M14: TRT 1s", 
    "M15: RTRT 2s", "M16: TRT 2s", 
    "M18: RTRT 3s", "M19: TRT 3s",
    "M20: Fun1 1s", "M21: Fun1 1s",
    "M20: Fun1 1s", "M21: Fun1 1s",
    "M22: Fun1 2s", "M23: Fun1 2s",
    "M24: Fun1 3s", "M25: Fun1 3s"
]
full_emotions = [
    "neutral", "sick", "vomit", "vomit2", "ready_to_race", "sad", "idle_stable", 
    "startled", "yes", "love_it", "chuckle", "blink_awake", "surprise"
]
emotions = full_emotions.copy()
index = 0
started = False
maneuver_task = None


# Helper functions    
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
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await x_controller.move_neg_x(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_5():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await x_controller.move_neg_x(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_9():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await x_controller.move_neg_x(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_2():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_1)
        await y_controller.neg_rot_y(duration=2*DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_6():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_2)
        await y_controller.neg_rot_y(duration=2*DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_10():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.neg_rot_y(duration=2*DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_3():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_7():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_11():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_4():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await x_controller.move_neg_x(DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_8():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await x_controller.move_neg_x(DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False
        
async def maneuver_12():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await x_controller.move_neg_x(DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_13():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_1)
        await x_controller.move_pos_x(DURATION_1)
        await y_controller.neg_rot_y(duration=DURATION_1)
        await x_controller.move_neg_x(2*DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_15():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_2)
        await x_controller.move_pos_x(DURATION_2)
        await y_controller.neg_rot_y(duration=DURATION_2)
        await x_controller.move_neg_x(2*DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_18():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_3)
        await x_controller.move_pos_x(DURATION_3)
        await y_controller.neg_rot_y(duration=DURATION_3)
        await x_controller.move_neg_x(2*DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_14():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
        await x_controller.move_pos_x(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_16():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
        await x_controller.move_pos_x(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_19():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await x_controller.move_pos_x(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_20():
    try:
        await asyncio.sleep_ms(2500)
        await y_controller.pos_rot_y(duration=DURATION_1)
        await y_controller.neg_rot_y(duration=DURATION_1)
        await y_controller.pos_rot_y(duration=DURATION_1)
        await y_controller.neg_rot_y(duration=DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_21():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_1)
        await x_controller.move_neg_x(DURATION_1)
        await x_controller.move_pos_x(DURATION_1)
        await x_controller.move_neg_x(DURATION_1)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_22():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_2)
        await y_controller.neg_rot_y(duration=DURATION_2)
        await y_controller.pos_rot_y(duration=DURATION_2)
        await y_controller.neg_rot_y(duration=DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_23():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_2)
        await x_controller.move_neg_x(DURATION_2)
        await x_controller.move_pos_x(DURATION_2)
        await x_controller.move_neg_x(DURATION_2)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_24():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.neg_rot_y(duration=DURATION_3)
        await y_controller.pos_rot_y(duration=DURATION_3)
        await y_controller.neg_rot_y(duration=DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def maneuver_25():
    try:
        await asyncio.sleep_ms(2500)
        play_random_emotion()
        await x_controller.move_pos_x(DURATION_3)
        await x_controller.move_neg_x(DURATION_3)
        await x_controller.move_pos_x(DURATION_3)
        await x_controller.move_neg_x(DURATION_3)
    except asyncio.CancelledError:
        stop_everything()
        raise
    finally:
        global started
        started = False

async def button_handler():
    global index, started, maneuver_task
    print(f"ASK,{maneuver_names[index]}")
    while True:
        await asyncio.sleep_ms(50)
        if board.is_select_pressed() and not started:
            await asyncio.sleep_ms(200)
            if board.is_select_pressed():
                index = (index + 1) % len(maneuver_names)
                print(f"ASK,{maneuver_names[index]}")
            while board.is_select_pressed():
                await asyncio.sleep_ms(20)

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
                    await asyncio.sleep(1)
                    coro = globals()[f"maneuver_{index+1}"]
                    maneuver_task = asyncio.create_task(coro())
            while board.is_start_stop_pressed():
                await asyncio.sleep_ms(20)

async def wait_for_connection():
    while not board.is_select_pressed():
        print("ASK,Connected.")
        await asyncio.sleep_ms(200)

async def main():
    await wait_for_connection()
    asyncio.create_task(button_handler())
    while True:
        await asyncio.sleep(1)

asyncio.run(main())