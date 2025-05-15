# Astrobee

Astrobee is a free-flying robotic platform originally developed by NASA for use inside the International Space Station (ISS). It is designed to autonomously assist astronauts by performing inspections, logistics operations, and other routine tasks. It uses air-based propulsion—specifically, fans and adjustable vents—to translate and rotate in microgravity environments without needing wheels or tracks.

Our project recreates a functional prototype of Astrobee using the XRP robotics platform. It incorporates embedded systems (STM32), custom control software, an LCD screen, and a localization mat of AprilTags. The system emulates Astrobee’s movement logic by coordinating brushless DC motors (fans) and servo-actuated vents to perform directional maneuvers during parabolic zero-gravity flights.

#### Up to date as of May 7, 2025.
![Astrobeen Replica with Labeled Vents](https://github.com/user-attachments/assets/233e7bd6-7513-4d07-aba8-a1956a2d583d)
*Figure 1: Our Astrobee replica with labeled vents and fan modules and coordinate system.*

---

## Propulsion System: Fans and Vents

Our replica uses:

* **2 inpellers** (brushless DC motors)
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
| Stop all motion | —                 | All vents closed |                                                   |

**Legend**
* **Vents A–F**: Labeled in image.
  
These calculations are detailed at [Astrobee Dynamics](https://humorous-scarer-601.notion.site/Astrobee-Dynamics-1ba5e61c54338086a670dc6c97f83654) and [Parameters](https://humorous-scarer-601.notion.site/Parameters-1c35e61c5433809589c2e20ca3862add).

---

## LCD Screen


---

## Localization
Lastly, we have a GoPro pointed in the –y direction, facing a mat of AprilTags mounted on the floor beneath the robot. The AprilTag mat is 5 feet by 5 feet and uses a 10x10 grid of 80mm wide tags and is included in this repository. 

During flight, the GoPro captures continuous downward-facing video of the AprilTag mat. Following the flight, we analyze the footage using computer vision algorithms to detect AprilTags in each frame and estimate the robot’s 2D position and orientation over time. This enables us to reconstruct the robot’s trajectory and quantify its displacement, providing a basis for post-flight evaluation of translation accuracy and maneuver performance.

An example script to detect AprilTags in every frame of a video is included in this repository. 

