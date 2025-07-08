# Screen-Recorder
Developed a Python-based screen recorder that captures full HD screen activity and saves it as a video file.
# 🎥 Screen Recording Automation using Python

A lightweight Python script that records full-screen activity and saves it as a high-quality `.mp4` video. Ideal for tutorials, monitoring, automation, and screen capture needs.

## 🚀 Features

- 📸 Real-time full-screen capture using `PyAutoGUI`
- 🎞️ Frame encoding and video writing with `OpenCV`
- 📐 Auto-detects screen resolution via `Win32API`
- 🎨 Accurate color rendering (RGB to BGR conversion)
- ⏱️ Customizable recording duration and frame rate
- 💾 Outputs `.mp4` or `.avi` files using modern codecs

---

## 🛠️ Tech Stack

- Python 3.x
- PyAutoGUI
- OpenCV (cv2)
- NumPy
- pywin32 (Win32API)

---

## 📄 How It Works

1. Gets your screen's current resolution.
2. Captures screenshots in real-time for a specified duration.
3. Converts each frame for OpenCV compatibility.
4. Encodes and saves the frames as a video (`.mp4` or `.avi`).

---

## 💻 Installation

Install the required packages:


pip install pyautogui opencv-python numpy pywin32

## 📁 Usage
Run the script:

bash
Copy
Edit
python screen_recorder.py

##📂 Output
A video file named test.mp4 will be saved in your working directory.

##🧪 Example Code Snippet
python
Copy
Edit
image = pyautogui.screenshot()
frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
output.write(frame)

## 📌 Use Cases
Video tutorials and demos

System monitoring or surveillance

Automated GUI testing and debugging

Screen-based task logging


