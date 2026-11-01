signal_length = 8        # seconds
sample_rate = 256        # Hz
num_samples = signal_length * sample_rate
freq_resolution = 1 / signal_length

print(f"Samples: {num_samples}")
print(f"Frequency resolution: {freq_resolution:.4f} Hz")