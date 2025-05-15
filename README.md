# Astrobee

Astrobee is a free-flying robotic platform originally developed by NASA for use inside the International Space Station (ISS). It is designed to autonomously assist astronauts by performing inspections, logistics operations, and other routine tasks. It uses air-based propulsion—specifically, fans and adjustable vents—to translate and rotate in microgravity environments without needing wheels or tracks.

Our project recreates a functional prototype of Astrobee using the XRP robotics platform. It incorporates embedded systems (STM32), custom control software, an LCD screen, and a localization mat of AprilTags. The system emulates Astrobee’s movement logic by coordinating brushless DC motors (fans) and servo-actuated vents to perform directional maneuvers during parabolic zero-gravity flights.

#### Up to date as of May 7, 2025.
![Astrobeen Replica with Labeled Vents](https://github.com/user-attachments/assets/233e7bd6-7513-4d07-aba8-a1956a2d583d)
*Figure 1: Our Astrobee replica with labeled vents and fan modules, and coordinate system.*

### Setting up the XRP
Connect the XRP that will be in the Astrobee via a USB-C cable to your computer. Run the script `setup.sh` included in this repository. Go to xrpcode.wpi.edu and run the script maneuvers_async_new.py and then disconnect the cable connecting the XRP to your computer.

### Operation
The interface supports two user-input buttons:

- Select button (blue): Cycles through a list of predefined maneuvers. Each press advances to the next maneuver and updates the display accordingly.

- Start/Stop button (green): Starts the currently displayed maneuver, or stops it if it is already in progress.

During a maneuver, the Astrobee will do the following:
1. Rise off of the ground.
2. Start playing random emotion on the screen.
3. Execute the steps in the maneuver.
4. Slowly fall back to the ground.

### Startup Procedure
1. Power on the Astrobee.
2. Wait for the LCD screen to boot to the desktop interface.
3. Use a stylus to tap the desktop file icon labeled PiZeroScript to launch the LCD control script.
4. Once the screen displays **"Connected."**, press the start/stop (green) button to begin interacting with the robot. 
   
### Normal Operation
1. Turn on the impellers. 
2. Press the **select** (blue) button to choose a maneuver. Each press advances to the next maneuver; this does not initiate the maneuver.
3. Press the **start/stop** (green) button to begin the currently displayed maneuver.
4. Wait for the maneuver to complete, or press the **start/stop** (green) button again to end it prematurely.
5. Repeat steps 2-4 to run additional maneuvers. 

### Shutdown Procedure
1. Turn off the impellers.
2. Power off the Astrobee system.

---

## Propulsion System: Fans and Vents

Our replica uses:

* **2 impellers** (brushless DC motors)
* **12 servo-controlled vents**, which open or close specific ducts to vector thrust and allow precise control of movement.

Each motion (translation or rotation) is achieved by **coordinated activation of both fans and directional opening of vents**.

### Mapping: Vent and Fan Activation for Motion

| **Movement**    | **Active Fan(s)** | **Open Vent(s)** | **Notes**                                         |
| --------------- | ----------------- | ---------------- | --------------------------------------------------|
| +x (right)      | Both Fans         | 11, 12           | Pushes air out rear to move right                 |
| –x (left)       | Both Fans         | 5, 6             | Pushes air out front to move left                 |
| +y (up)         | Both Fans         | 3, 9             | Pushes air out right to move up                   |
| –y (down)       | Both Fans         | 1, 7             | Pushes air out left to move down                  |
| +z (forward)    | Both Fans         | 4, 8             | Pushes air out right to move forward              |
| –z (backward)   | Both Fans         | 2, 10            | Pushes air out left to move backward              |
| +Rx             | Both Fans         | 1, 3  or 8, 10   | First set and second set produce the same torque. |
| -Rx             | Both Fans         | 2, 4  or 7, 9    | First set and second set produce the same torque. |
| +Ry             | Both Fans         | 2, 8  or 5, 11   | First set produces bigger torque.                 |
| -Ry             | Both Fans         | 4, 10 or 6, 12   | First set produces bigger torque.                 |
| +Rz             | Both Fans         | 3, 7  or 5, 12   | First set produces bigger torque.                 |
| -Rz             | Both Fans         | 1, 9  or 6, 11   | First set produces bigger torque.                 |
| Stop all motion | —                 | All vents closed | Halts all translation and rotation.               |

**Legend**
* **Vents 1-12**: Labeled in figure 1.

Detailed calculations are documented in:

- [Astrobee Dynamics](https://humorous-scarer-601.notion.site/Astrobee-Dynamics-1ba5e61c54338086a670dc6c97f83654)
- [Parameters](https://humorous-scarer-601.notion.site/Parameters-1c35e61c5433809589c2e20ca3862add)

---

## LCD Screen
The Astrobee replica includes an onboard LCD screen connected to a Raspberry Pi 0, which acts as a display to see what maneuver is being selected or animated emotional expressions. 

- The LCD screen connects to the Raspberry Pi 0 via GPIO pins.
- The XRP is connected to the Raspberry Pi 0 via a USB-C to MicroUSB cable.
- The XRP communicates with the Raspberry Pi 0 via USB serial, sending messages over /dev/ttyACM0

The Raspberry Pi 0 is flashed with a preconfigured disk images, available in this repository. It includes:
- the Raspberry Pi 0 settings needed to read serial communication
- the [cs-rereminibot](https://github.com/cornell-cup/cs-rereminibot) repository, which contains the Python script that
   - Listens for incoming messages from the XRP.
   - Displays the currently selected maneuver.
   - Plays a randomly chosen emotional expression during active maneuvers.
     
To launch the LCD script, use a stylus to tap the PiZeroScript file icon on the desktop screen that appears after boot. The screen will show “Connected.” once serial communication is established.

Note: To verify that the Raspberry Pi has recognized the XRP, run lsusb—a connected MicroPython board should appear in the output.

---

## Localization
To evaluate maneuver performance, the Astrobee includes a visual localization system based on AprilTags. A GoPro is mounted facing the –y direction, recording the robot’s motion over a 5 ft × 5 ft AprilTag mat placed on the floor.

- The mat consists of a 10×10 grid of 80 mm-wide tags, included in this repository.
- During flight, the GoPro continuously records downward-facing video.
- After flight, we analyze the footage using computer vision algorithms to:
  - Detect AprilTags in each frame.
  - Estimate the robot’s 2D position and orientation over time.

This enables accurate trajectory reconstruction and quantitative evaluation of displacement and control accuracy.

An example script for detecting AprilTags in each video frame is included in this repository.

