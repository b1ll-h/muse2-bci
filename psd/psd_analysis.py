import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch

# --- Load your real EEG data ---
df = pd.read_csv("/Users/williamhsu/EEG_recording_2026-05-03-05.54.02.csv")
print(df.head())
print(f"Total samples: {len(df)}")

# --- Extract AF7 channel (left forehead — best for attention/relaxation) ---
sample_rate = 256
channel = df["AF7"].values

# --- Calculate PSD using Welch method ---
frequencies, power = welch(channel, fs=sample_rate, nperseg=256)

# --- Plot it ---
plt.figure(figsize=(10, 4))
plt.plot(frequencies, power)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power (µV²/Hz)")
plt.title("Power Spectral Density — AF7 Channel (Your Real Brainwaves)")
plt.xlim(0, 50)

# Draw vertical lines at band boundaries
plt.axvline(x=4,  color="gray",  linestyle="--", alpha=0.7, label="delta/theta (4 Hz)")
plt.axvline(x=8,  color="blue",  linestyle="--", alpha=0.7, label="theta/alpha (8 Hz)")
plt.axvline(x=13, color="green", linestyle="--", alpha=0.7, label="alpha/beta (13 Hz)")
plt.axvline(x=30, color="red",   linestyle="--", alpha=0.7, label="beta/gamma (30 Hz)")

plt.legend()
plt.tight_layout()
plt.show()