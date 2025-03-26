Overview

This repository contains a Python script that visualizes how the radiation energy of a black body changes with temperature. The graph is based on Planck’s Law, which describes the spectral distribution of electromagnetic radiation emitted by an ideal black body.


Features

✅ Plots black body radiation curves for different temperatures
✅ Uses Planck’s Law to compute spectral radiance
✅ Customizable wavelength range and temperature values
✅ Simple and clean visualization


Example Output

![image](https://github.com/user-attachments/assets/b12af4b2-b225-4c77-9025-4338008dae35)


Scientific Background

This visualization is based on Planck’s Law, given by:
B(\lambda, T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\frac{hc}{\lambda k T}} - 1}
where:
	•	B(\lambda, T) is the spectral radiance,
	•	h is Planck’s constant,
	•	c is the speed of light,
	•	k is Boltzmann’s constant,
	•	\lambda is the wavelength,
	•	T is the absolute temperature (Kelvin).

As temperature increases, the peak of the radiation curve shifts to shorter wavelengths (Wien’s Displacement Law) and the total emitted energy increases (Stefan-Boltzmann Law).
