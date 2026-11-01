TP9 = [24, 35, 2, 8, 15, 42, 80, 28]
AF7 = [12, 45, 27, 102, 11, 45, 67, 89]
AF8 = [88, 23, 9, 56, 78, 108, 34, 67]
TP10 = [34, 67, 89, 12, 45, 23, 56, 78]
channels = [TP9, AF7, AF8, TP10]
names = ["TP9", "AF7", "AF8", "TP10"]
frequencies = [10, 22, 3, 35]

for i in range(len(channels)):
    total = 0
    artifact_count = 0
    warning_count = 0
    for v in channels[i]:
        total = total + v
        if v > 80:
            artifact_count = artifact_count + 1
        if v >= 60 and v <= 80:
            warning_count = warning_count + 1
    average = total / len(channels[i])
    
    if artifact_count == 0:
        status = "GOOD"
    elif artifact_count >= 1 and artifact_count <= 2:
        status = "NOISY"
    else:
        status = "BAD"
    f = frequencies[i]
    if f < 4:
        band = "Delta"
    elif f >= 4 and f < 8:
        band = "Theta"
    elif f >= 8 and f < 13:
        band = "Alpha"
    elif f >= 13 and f < 30:
        band = "Beta"
    else:
        band = "Gamma"
    print(f"--- Channel {names[i]} ---")
    print(f"Avg voltage: {average:.2f} uV")
    print(f"Artifacts: {artifact_count} | Status: {status}")
    print(f"Dominant Frequency: {f} Hz | Band: {band}")
    print()