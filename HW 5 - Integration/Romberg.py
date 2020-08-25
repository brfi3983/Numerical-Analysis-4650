import numpy as np
import math

# ====================================================
def f(x):
	return (math.sin(x)**2 - 2*x*math.sin(x) + 1)

# ====================================================
def R(k, j, a, b):

	# Break out condition
	if j == 1:
		return R_1(k, a, b)
	
	# Recursive formula for Rhomerg greater than 1 
	val = R(k, j - 1, a, b) + (4**(j - 1) - 1)**(-1)*(R(k, j - 1, a, b) - R(k - 1, j - 1, a, b))
	return val

# ====================================================
def R_1(k,a,b):
	# Defining h
	h = b - a

	# Finding middle sum
	total = 0
	for i in range(0, 2**(k-1)-1):
		total += f(a + (i+1)*(h / 2**(k - 1)))
	
	# Caculating R
	R = (h/2**(k))*(f(a) + f(b) + 2*total)

	return R

# ====================================================
def main():
	a = 1
	b = 4
	x = R(3,3, a, b)
	print(x)

	X = 8*math.cos(4) -2*math.sin(4) -2*math.cos(1) + 2*math.sin(1) + 9/2 + (-math.sin(8) + math.sin(2))/4
	print(X)

# ====================================================
if __name__ == "__main__":
	main()
