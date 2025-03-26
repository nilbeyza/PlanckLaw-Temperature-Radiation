import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34  # Planck's constant (Joule·s)
c = 3e8  # Speed of light (m/s)
k_B = 1.381e-23  # Boltzmann's constant (Joule/K)

temperatures = [2000, 3000, 4000, 5000, 6000, 7000]

lambda_values = np.linspace(10e-9, 3000e-9, 1000)  # Meters

plt.figure(figsize=(10, 6))

for T in temperatures:
    B_lambda = (2 * h * c**2) / ((lambda_values + 1e-12)**5 * np.expm1(h * c / ((lambda_values + 1e-12) * k_B * T)))
    plt.plot(lambda_values * 1e9, B_lambda, label=f"T = {T} K")

plt.title("Black Body Radiation Curve at Different Temperatures")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Spectral Radiance B(λ) (W·sr⁻¹·m⁻³)")
plt.legend()
plt.grid(True)

plt.show()
