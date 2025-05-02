import cv2
import numpy as np
from pupil_apriltags import Detector

# === USER CONFIGURATION ===
# video_path = "/Users/SanjanaNandi/Desktop/GX010001.MP4"         # Replace with your GoPro video file
# video_path = "/Users/SanjanaNandi/Desktop/GX010020.MP4"
video_path = "/Users/SanjanaNandi/Desktop/GX010019.MP4"

frame_skip = 10                      # Process every Nth frame for speed
resize_width = 1280                 # Resize width for faster detection (set None to skip)
display = True                      # Show live preview with detections

# === APRILTAG DETECTOR SETUP ===
detector = Detector(
    families='tag36h11',
    nthreads=4,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=True,
    decode_sharpening=0.25,
    debug=False
)

# === LOAD VIDEO ===
cap = cv2.VideoCapture(video_path)
frame_count = 0
detected_total = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip != 0:
        continue

    # Resize for speed (optional)
    if resize_width:
        h, w = frame.shape[:2]
        scale = resize_width / w
        frame = cv2.resize(frame, (resize_width, int(h * scale)))

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Sharpen the image (helps with blurry tags)
    sharpen_kernel = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
    sharp = cv2.filter2D(gray, -1, sharpen_kernel)

    # Detect tags
    detections = detector.detect(
        sharp,
        estimate_tag_pose=False,
        camera_params=None,
        tag_size=None
    )
    detected_total += len(detections)

    if display:
        for det in detections:
            pts = np.int32(det.corners)
            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
            cx, cy = int(det.center[0]), int(det.center[1])
            cv2.putText(frame, f"ID {det.tag_id}", (cx, cy), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)

        cv2.imshow('AprilTag Detection (pupil_apriltags)', frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print(f"Total detections: {detected_total} frames with tags")