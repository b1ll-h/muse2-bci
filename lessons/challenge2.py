frequency_readings = [1, 42, 26, 7, 11, 3, 19, 37]
delta_count = 0
theta_count = 0
alpha_count = 0
beta_count = 0
gamma_count = 0

for f in frequency_readings:
    if f < 4:
        delta_count = delta_count + 1
        print(f"{f} Hz —> delta wave")
    elif f >= 4 and f < 8:
        theta_count = theta_count + 1
        print(f"{f} Hz —> theta wave")
    elif f >= 8 and f < 13:
        alpha_count = alpha_count + 1
        print(f"{f} Hz —> alpha wave")
    elif f >= 13 and f < 30:
        beta_count = beta_count + 1
        print(f"{f} Hz —> beta wave")
    elif f >= 30:
        gamma_count = gamma_count + 1
        print(f"{f} Hz —> gamma wave")

print(f"Delta: {delta_count}")
print(f"Theta: {theta_count}")
print(f"Alpha: {alpha_count}")
print(f"Beta: {beta_count}")
print(f"Gamma: {gamma_count}")