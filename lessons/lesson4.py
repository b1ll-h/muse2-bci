eeg_signal = [5.2, 78.3, 34.1, 92.4, 11.8, 45.6, 88.2, 23.9]
total = 0

for voltage in eeg_signal:
    total = total + voltage

average = total / len(eeg_signal)
print(f"Total: {total:.2f}")
print(f"Number of samples: {len(eeg_signal)}")
print(f"Average voltage: {average:.2f} microvolts")

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num
    print(f"Just added {num}. Total is now: {total}")  # ← indented

print(f"\nFinal total: {total}")  # ← NOT indented