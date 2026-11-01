channel = "Fp1"
voltage = 63.4821
sample = 142
rate = 256

print(f"Channel: {channel}")
print(f"Voltage: {voltage:.2f} uV")
print(f"Voltage (4 decimal places): {voltage:.4f} uV")
print(f"Sample {sample} of {rate} — time: {sample / rate:.4f} seconds")
print()
print(f"Brainwaves: {'delta'}, {'theta'}, {'alpha'}, {'beta'}, {'gamma'}", sep=" | ")