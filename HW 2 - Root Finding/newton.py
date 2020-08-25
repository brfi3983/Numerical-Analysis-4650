<<<<<<< HEAD
import math
import numpy as np

# ====================================================================
def g_func(x):
	return math.log(x - 1) + math.cos(x - 1)

# ====================================================================
def g_func_prime(x):
	return 1/(x-1) - math.sin(x - 1)

# ====================================================================
def newton(p_0, TOL, N_0):
	# declare and define i
	i = 1

	# Newtons method after calling upon function and function prime values
	while i <= N_0:
		p = p_0 - g_func(p_0)/g_func_prime(p_0)
		if abs(p - p_0) < TOL:
			return p
		i += 1
		p_0 = p

	return 'Not enough Iterations'

# =====================================================================
def main():
	# Define constants and criteria
	p_0 = 1.5
	TOL = 10e-8
	N_0 = 10
	root_true = newton(p_0, TOL, N_0)
	
	# Find interval by iterating by a 0.001 until the root no longer can be found 
	# (this method did not work, however, and returned an epsilon of 0 around p_0 = 1.5)

	# Find right endpoint
	i = 0
	while i < 100:
		root_temp = newton(p_0 + i - 0.001, TOL, N_0)
		root = newton(p_0 + i, TOL, N_0)
		if root != root_true:
			min_a = root_temp
			break
		i += 0.001

	# Find left endpoint
	i = 0
	while i < 100:
		root_temp = newton(p_0 - i + 0.001, TOL, N_0)
		root = newton(p_0 - i, TOL, N_0)
		if root != root_true:
			max_a = root_temp
			break
		i -= 0.001
	
	# Output endpoints found
	print("Left endpoint:", min_a,"\nRight endpoint:", max_a)

# =======================================================================
if __name__ == "__main__":
	main()
=======
import math
import numpy as np

# ====================================================================
def g_func(x):
	return math.log(x - 1) + math.cos(x - 1)

# ====================================================================
def g_func_prime(x):
	return 1/(x-1) - math.sin(x - 1)

# ====================================================================
def newton(p_0, TOL, N_0):
	# declare and define i
	i = 1

	# Newtons method after calling upon function and function prime values
	while i <= N_0:
		p = p_0 - g_func(p_0)/g_func_prime(p_0)
		if abs(p - p_0) < TOL:
			return p
		i += 1
		p_0 = p

	return 'Not enough Iterations'

# =====================================================================
def main():
	# Define constants and criteria
	p_0 = 1.5
	TOL = 10e-8
	N_0 = 10
	root_true = newton(p_0, TOL, N_0)
	
	# Find interval by iterating by a 0.001 until the root no longer can be found 
	# (this method did not work, however, and returned an epsilon of 0 around p_0 = 1.5)

	# Find right endpoint
	i = 0
	while i < 100:
		root_temp = newton(p_0 + i - 0.001, TOL, N_0)
		root = newton(p_0 + i, TOL, N_0)
		if root != root_true:
			min_a = root_temp
			break
		i += 0.001

	# Find left endpoint
	i = 0
	while i < 100:
		root_temp = newton(p_0 - i + 0.001, TOL, N_0)
		root = newton(p_0 - i, TOL, N_0)
		if root != root_true:
			max_a = root_temp
			break
		i -= 0.001
	
	# Output endpoints found
	print("Left endpoint:", min_a,"\nRight endpoint:", max_a)

# =======================================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
