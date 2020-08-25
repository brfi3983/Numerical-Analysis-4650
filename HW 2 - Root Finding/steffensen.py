import math

# ====================================================
def g(x):
	return 2 + math.sin(x)

# ====================================================
def steff(p_0, TOL, N_0, ptrue):
	# Define and declare i
	i = 1

	# Use Steffensen method and fixed point to approximate quadratically and output absolute error for each step
	while i <= N_0:

		# Call function
		p_1 = g(p_0)
		p_2 = g(p_1)

		# Approximate via steffensen method
		p = p_0 - (p_1 - p_0)**2 / (p_2 - 2*p_1 + p_0)

		# Find error
		abs_error = abs(ptrue - p)
		print('p value:', p, 'Absolute Error:', abs_error)

		# Return approximation if below tolerence for accuracy
		if abs(p - p_0) < TOL:
			return p, i
		i += 1
		p_0 = p

	return 'Error'

# ====================================================
def main():

	# Define constants and criteria
	p_0 = 2
	N_0 = 100
	TOL = 10e-9
	ptrue = 2.554195952837043

	# Steffensen method
	pt, i = steff(p_0, TOL, N_0, ptrue)

# ====================================================
if __name__ == "__main__":
	main()
