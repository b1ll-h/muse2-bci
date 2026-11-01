eeg_signal = [12.3, 45.1, 23.7, 102.4, 11.8, 45.6, 88.2, 23.9]
sample_rate = 256
threshold_high = 100.0    # microvolts — definitely an artifact
threshold_warn = 75.0     # microvolts — suspicious

clean_samples = 0
warnings = 0
artifacts = 0

for i, voltage in enumerate(eeg_signal):
    if voltage > threshold_high:
        print(f"Sample {i}: {voltage:.1f} uV ← ARTIFACT")
        artifacts = artifacts + 1
    elif voltage > threshold_warn:
        print(f"Sample {i}: {voltage:.1f} uV ← WARNING")
        warnings = warnings + 1
    else:
        print(f"Sample {i}: {voltage:.1f} uV ✓ clean")
        clean_samples = clean_samples + 1

print(f"\nSummary:")
print(f"Clean samples: {clean_samples}")
print(f"Warnings: {warnings}")
print(f"Artifacts: {artifacts}")