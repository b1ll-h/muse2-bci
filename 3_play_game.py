import numpy as np
import pyautogui
import time
from pylsl import StreamInlet, resolve_byprop
from collections import deque

SAMPLE_RATE = 256
COOLDOWN = 0.4
WINDOW_SIZE = 256 * 1
MULTIPLIER = 1.8
MIN_BLINK_SAMPLES = 4
MAX_BLINK_SAMPLES = 60

print("Looking for EEG stream...")
streams = resolve_byprop("type", "EEG", timeout=10)
if len(streams) == 0:
    print("No stream found!")
    exit()

inlet = StreamInlet(streams[0])
print("Connected! Calibrating for 5 seconds — sit still...")
time.sleep(5)
print("Starting in 3 seconds — switch to Geometry Dash!")
time.sleep(3)
print("Running! Blink to jump. Press Ctrl+C to stop.")

last_jump_time = 0
baseline_window = deque(maxlen=WINDOW_SIZE)
above_threshold_count = 0

while True:
    sample, timestamp = inlet.pull_sample()

    af7 = abs(sample[1])
    af8 = abs(sample[2])
    signal = max(af7, af8)

    baseline_window.append(signal)

    if len(baseline_window) < WINDOW_SIZE:
        continue

    baseline = np.percentile(list(baseline_window), 50)
    threshold = baseline * MULTIPLIER
    current_time = time.time()

        # Hard ignore window right after a jump
    if current_time - last_jump_time < COOLDOWN:
        above_threshold_count = 0
        continue

    if signal > threshold:
        above_threshold_count += 1
    else:
        if MIN_BLINK_SAMPLES <= above_threshold_count <= MAX_BLINK_SAMPLES:
            pyautogui.press("space")
            print(f"BLINK! duration={above_threshold_count} samples → jumped!")
            last_jump_time = current_time
        above_threshold_count = 0