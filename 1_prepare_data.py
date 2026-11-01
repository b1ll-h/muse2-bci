import numpy as np
import pandas as pd
from scipy.signal import welch

SAMPLE_RATE = 256
EPOCH_SIZE = 256 * 1
CHANNELS = ["TP9", "AF7", "AF8", "TP10"]

BANDS = {
    "delta": (0.5, 4),
    "theta": (4, 8),
    "alpha": (8, 13),
    "beta":  (13, 30),
    "gamma": (30, 40)
}

def get_band_power(psd_freqs, psd_power, band):
    low, high = band
    idx = np.where((psd_freqs >= low) & (psd_freqs <= high))[0]
    return np.mean(psd_power[idx])

def extract_features(epoch):
    features = []
    for ch in CHANNELS:
        signal = epoch[ch].values
        freqs, power = welch(signal, fs=SAMPLE_RATE, nperseg=SAMPLE_RATE)
        for band_name, band_range in BANDS.items():
            bp = get_band_power(freqs, power, band_range)
            features.append(np.log(bp + 1e-10))
    return features

def process_file(filepath, label):
    print(f"Processing {filepath}...")
    df = pd.read_csv(filepath)
    print(f"  Rows: {len(df)}")
    df = df[CHANNELS]
    df = df.dropna()
    features_list = []
    labels_list = []
    num_epochs = len(df) // EPOCH_SIZE
    print(f"  Found {num_epochs} epochs")
    for i in range(num_epochs):
        start = i * EPOCH_SIZE
        end = start + EPOCH_SIZE
        epoch = df.iloc[start:end]
        features = extract_features(epoch)
        features_list.append(features)
        labels_list.append(label)
    return features_list, labels_list

files = [
    ("/Users/williamhsu/Desktop/python_lessons/EEG_noblink.csv", 0),
    ("/Users/williamhsu/Desktop/python_lessons/EEG_blink.csv",   1)
]

all_features = []
all_labels = []

for filepath, label in files:
    try:
        f, l = process_file(filepath, label)
        all_features.extend(f)
        all_labels.extend(l)
    except FileNotFoundError:
        print(f"  WARNING: {filepath} not found, skipping...")

X = np.array(all_features)
y = np.array(all_labels)

print(f"\nTotal epochs: {len(X)}")
print(f"Feature vector size: {X.shape[1]}")
print(f"Labels: {np.unique(y, return_counts=True)}")

np.save("X.npy", X)
np.save("y.npy", y)
print("\nSaved X.npy and y.npy — ready for training!")
