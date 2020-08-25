import numpy as np
import math

# ====================================================
def func(x):
	return (x**2)*math.exp(x)

# ====================================================
def absolute_error(true, computed):
	return abs(true - computed)

# ====================================================
def ForwardDifference(x_0, n_upper, true):
	# Preallocating
	arr = np.zeros((n_upper, 3), dtype= np.float32)

	# Creating table
	for i in range (0, n_upper):
		h = 10**(-(i + 1))
		val = (func(x_0 + h) - func(x_0)) / h
		arr[i, 0] = i + 1
		arr[i, 1] = val
		arr[i, 2] = absolute_error(true, val)
	return arr

# ====================================================
def main():
	table = ForwardDifference(3, 20, 301.28305)
	print(table)

# ====================================================
if __name__ == "__main__":
	main()
