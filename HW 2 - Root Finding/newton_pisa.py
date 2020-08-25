<<<<<<< HEAD
import math
import numpy as np

# ===================================================
def g_func(x):
	return x**3 + 2*x**2 + 10*x - 20

# ===================================================
def g_func_prime(x):
	return 3*x**2 + 4*x + 10

# ===================================================
def f_true():
	# Pisa's approxmiation
	x = 1 + 22*(1/60) + 7*(1/60)**2 + 42*(1/60)**3 + \
            33*(1/60)**4 + 4*(1/60)**5 + 40*(1/60)**6
	return x

# ===================================================
def newton(p_0, TOL, N_0, ptrue):
	i = 1
	while i <= N_0:
		# Exiting Newton's when error is within threshold
		p = p_0 - g_func(p_0)/g_func_prime(p_0)
		if abs(p - p_0) < TOL:
			print('Absolute Error:', abs(p - ptrue))
			return p, i
		i += 1
		p_0 = p

	return 'Not enough Iterations'

# ===================================================
def main():
	# Define constants and criteria
	p_0 = 2
	TOL = 10e-14
	N_0 = 100

	# Find true value (or at least what Pisa approximated)
	ptrue = f_true()

	# Find approimation via newton and compare to Pisa
	pt, j = newton(p_0, TOL, N_0, ptrue)

# ===================================================
if __name__ == "__main__":
	main()
=======
import math
import numpy as np

# ===================================================
def g_func(x):
	return x**3 + 2*x**2 + 10*x - 20

# ===================================================
def g_func_prime(x):
	return 3*x**2 + 4*x + 10

# ===================================================
def f_true():
	# Pisa's approxmiation
	x = 1 + 22*(1/60) + 7*(1/60)**2 + 42*(1/60)**3 + \
            33*(1/60)**4 + 4*(1/60)**5 + 40*(1/60)**6
	return x

# ===================================================
def newton(p_0, TOL, N_0, ptrue):
	i = 1
	while i <= N_0:
		# Exiting Newton's when error is within threshold
		p = p_0 - g_func(p_0)/g_func_prime(p_0)
		if abs(p - p_0) < TOL:
			print('Absolute Error:', abs(p - ptrue))
			return p, i
		i += 1
		p_0 = p

	return 'Not enough Iterations'

# ===================================================
def main():
	# Define constants and criteria
	p_0 = 2
	TOL = 10e-14
	N_0 = 100

	# Find true value (or at least what Pisa approximated)
	ptrue = f_true()

	# Find approimation via newton and compare to Pisa
	pt, j = newton(p_0, TOL, N_0, ptrue)

# ===================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
