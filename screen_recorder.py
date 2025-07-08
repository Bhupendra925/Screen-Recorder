import pyautogui
import cv2
import numpy as np
from win32api import GetSystemMetrics
import time

# Get screen resolution
width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)
dim = (width, heigth)

# Define video codec and output file
f = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4", f, 30.0, dim)

# Set recording duration
now_start_time = time.time()
dur = 10  # in seconds
end_time = now_start_time + dur

# Start screen recording
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)

    if time.time() > end_time:
        break

# Release the video file and print end message
output.release()
print("--- END ---")

              
      














