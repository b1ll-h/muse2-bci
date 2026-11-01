TP9 = [24, 35, 2, 8, 15, 42]
AF7 = [12, 45, 27, 102, 11, 45]
AF8 = [88, 23, 9, 56, 78, 108]
TP10 = [34, 67, 89, 12, 45, 23]

channels = [TP9, AF7, AF8, TP10]
names = ["TP9", "AF7", "AF8", "TP10"]


for i in range(len(channels)):
    total = 0
    artifact_count = 0
    for v in channels[i]:
        total = total + v
        if v > 80:
            artifact_count = artifact_count + 1
    average = total / len(channels[i])
    if artifact_count == 0:
        status = "GOOD"
    elif artifact_count >= 1 and artifact_count <= 2:
        status = "NOISY"
    else:
        status = "BAD"
    print(f"Channel {names[i]} | Avg: {average:.2f} uV | Artifacts: {artifact_count} | Status: {status}")