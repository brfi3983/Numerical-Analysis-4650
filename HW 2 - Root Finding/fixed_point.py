<<<<<<< HEAD
import math

# =====================================
def g_func(x):
	return math.pi + 0.5*math.sin(x/2)

# =====================================
def fixed_pt(p_0, TOL, N_0):
	# Define and declare i
	i = 1

	# Iterate through by calling on g and using fixed point method
	while i <= N_0: 
		p = g_func(p_0)
		if abs(p_0 - p) < TOL:
			return p, i
		i += 1
		p_0 = p

	return 'Error'

# =====================================
def main():
	# Define constants and criteria
	p_0 = 1
	TOL = 10e-10
	N_0 = 100

	# Find approximation via fixed point method
	pt, it_num = fixed_pt(p_0, TOL, N_0)
	print("Approximation:", pt, "Number of Iterations:", it_num)

# =====================================
if __name__ == "__main__":
	main()
=======
import math

# =====================================
def g_func(x):
	return math.pi + 0.5*math.sin(x/2)

# =====================================
def fixed_pt(p_0, TOL, N_0):
	# Define and declare i
	i = 1

	# Iterate through by calling on g and using fixed point method
	while i <= N_0: 
		p = g_func(p_0)
		if abs(p_0 - p) < TOL:
			return p, i
		i += 1
		p_0 = p

	return 'Error'

# =====================================
def main():
	# Define constants and criteria
	p_0 = 1
	TOL = 10e-10
	N_0 = 100

	# Find approximation via fixed point method
	pt, it_num = fixed_pt(p_0, TOL, N_0)
	print("Approximation:", pt, "Number of Iterations:", it_num)

# =====================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
