voltage = [12.3, 45.1, 23.7, 102.4, 78.3, 50.2, 88.3, 111.9, 21.5, 34.6]

artifact_count = 0
warning_count = 0
clean_count = 0
total = 0

for v in voltage:
    total = total + v
    if v > 80.0:
        print(f"{v} uV ← ARTIFACT")
        artifact_count = artifact_count + 1
    elif v >= 60.0 and v <= 80.0:
        print(f"{v} uV ← WARNING")
        warning_count = warning_count + 1
    else:
        print(f"{v} uV ← CLEAN")
        clean_count = clean_count + 1

average = total / len(voltage)
print(f"Total samples: {len(voltage)}")
print(f"Average voltage: {average:.2f} microvolts")
print(f"Clean: {clean_count}")
print(f"Warning: {warning_count}")
print(f"Artifact: {artifact_count}")