import numpy as np
import math

# ====================================================
def func(x):
	return math.sin(6*x)**2*math.exp(4*x)

# ====================================================
def SimpsonRuleApprox(x_0, x_2, h):
	return (h/3)*(func(x_0) + 4*func((x_0 + x_2)/2) + func(x_2))

# ====================================================
def SimpsonRuleComposite(a, n, h):
	total = 0

	# Summing individual Simpsons along partial curve
	for j in range(0, n):
		total += SimpsonRuleApprox(a + j*h, h*(1+j), h)
	total = total / 2
	return total

# ====================================================
def abs_error_specific(computed):
	true = 7.2349537666079042
	return abs(true - computed)

# ====================================================
def main():
	a = 0
	b = 1
	n = 1000
	h = (b - a) / n

	approx = SimpsonRuleComposite(a, n, h)
	print('n:', n , '| Approximation:', approx, '| Error:', abs_error_specific(approx))

# ====================================================
if __name__ == "__main__":
	main()

