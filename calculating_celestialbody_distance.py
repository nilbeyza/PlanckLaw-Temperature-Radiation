import numpy as np

# --- Constants ---
wien_b = 2.898e-3  # Wien's displacement constant (m·K)
sigma = 5.670374419e-8  # Stefan–Boltzmann constant (W/m²·K⁴)

# --- Example: Sun data ---
lambda_max_nm = 500  # Peak wavelength (nm)
lambda_max_m = lambda_max_nm * 1e-9  # Convert nm to meters

F = 1361  # Solar irradiance at Earth (W/m²)
R = 6.96e8  # Radius of the Sun (m)

# --- Calculate temperature using Wien's law ---
T = wien_b / lambda_max_m

# --- Calculate total radiant power using the Stefan–Boltzmann law ---
L = 4 * np.pi * R**2 * sigma * T**4

# --- Calculate distance to Earth using the inverse-square law ---
d = np.sqrt(L / (4 * np.pi * F))

# --- Print results ---
print(f"Temperature of the celestial body: {T:.2f} K")
print(f"Distance of the celestial body: {d / 1.496e11:.2f} AU")
