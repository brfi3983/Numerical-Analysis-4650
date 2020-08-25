import math

# ====================================================
def SqrtFinder(num, a, b):
	# Counter
	n = 0
	N_0 = 10

	# Equations for input
	y1 = a**2 - num
	y2 = b**2 - num

	# Tolerance, 10 decimals
	TOL = 1e-10

	# For loop via the bisection method
	for i in range (0,N_0):
		n = n + 1
		c = (a+b)/2
		y = c**2 - num
		print("a_" + str(n) + ":", a, "b_" + str(n) + ":", b)
		if y == 0 or abs(y) <= TOL:
			break
		elif y*y1 < 0:
			b = c
		else:
			a = c

	return c

# ====================================================
def ExponentSquare(num, a, b):
	# Counter
	n = 0
	N_0 = 40

	# Equations for input
	y1 = num**a - a**2
	y2 = num**b - b**2

	# Tolerance, 10 decimals
	TOL = 1e-10

	# For loop
	for i in range(0, N_0):
		n = n + 1
		c = (a+b)/2
		y = num**c - c**2
		if y == 0 or abs(y) <= TOL:
			break
		elif y*y1 < 0:
			b = c
		else:
			a = c

	return c

# ====================================================
def error(p, ptrue):
	# Takes in true and measured values and returns absolute and relative error
	abs_error = abs(p - ptrue)
	rel_error = abs_error / ptrue

	return abs_error, rel_error
# ====================================================
def main():
	# Define interval and number to find
	a1 = 1
	b1 = 2
	num = 2

	ans = SqrtFinder(num, a1, b1)
	print("\nThe root is approx. :", ans)

	# Use library to find true value
	ptrue = math.sqrt(2)

	# Find Absolute and Relative error
	abs_error, rel_error = error(ans, ptrue)
	print("Absolute Error:", abs_error, "\nRelative Error:",rel_error)

# ====================================================
if __name__ == "__main__":
	main()
