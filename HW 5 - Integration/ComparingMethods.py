import numpy as np
import math

# ====================================================
def f(x):
	return (math.cos(2*x) + math.exp(x**2) + 3) / (4 + math.sin(4*x))

# ====================================================
def SimpsonRuleApprox(x_0, x_2, h):
	return (h/3)*(f(x_0) + 4*f((x_0 + x_2)/2) + f(x_2))

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
	true = 2.5289360549014543
	return abs(true - computed)

# ====================================================
def R(k, j, a, b):

	# Break out condition
	if j == 1:
		return R_1(k, a, b)

	# Recursive formula for Rhomberg greater than 1
	val = R(k, j - 1, a, b) + (4**(j - 1) - 1)**(-1) * \
	        (R(k, j - 1, a, b) - R(k - 1, j - 1, a, b))
	return val

# ====================================================
def R_1(k, a, b):
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
def f_transform(y, a1, a2):
	x = a1 + a2*y
	return a2*f(x)

# ====================================================
def interval_transform(a, b):

	# Transforming interval from (a, b) into (-1, 1)
	a_arr = np.array([[1, -1], [1, 1]])
	b_vec = np.array([a, b])
	a1, a2 = np.linalg.solve(a_arr, b_vec)
	return a1, a2

# ====================================================
def LegrengeRoots(n):

	# Obtaining roots from local storage
	roots = np.genfromtxt(
		"C:/Users/user/Documents/School/2019-2020/APPM 4650/Roots.csv", delimiter=",")
	roots[0][0] = 1

	# Arrays
	nodes = np.zeros((n - 1))
	weights = np.zeros((n - 1))

	# Finding indices
	ind = -1
	for i in range(0, roots.shape[0]):
		if roots[i, 0] == n:
			ind = i

	# Storing roots and weights from file
	nodes = roots[ind:ind + n, 1]
	weights = roots[ind:ind + n, 2]
	return nodes, weights

# ====================================================
def Guassian(a, b, n):

	# Whole process of guassian quadrature
	a1, a2 = interval_transform(a, b)
	nodes, weights = LegrengeRoots(n)
	f_arr = np.zeros((len(nodes)))
	for i in range(0, len(nodes)):
		f_arr[i] = f_transform(nodes[i], a1, a2)
	I = np.dot(weights, f_arr)
	return I

# ====================================================
def NinePtNewtonCotes(x_0, x_8):

	# Numerical method to compare
	h = (x_8 - x_0) / 9
	I = (4*h/14175)*(989*f(x_0) + 5888*f(x_0 + h) - 928 *
                  f(x_0 + 2*h) + 10496*f(x_0 + 3*h) - 4540*f(x_0 + 4*h) +
                  10496*f(x_0 + 5*h) - 928*f(x_0 + 6*h) + 5888*f(x_0 + 7*h) + 989*f(x_0 + 8*h))
	return I

# ====================================================
def main():

	# Bounds
	a = -1
	b = 1

	# Simpsons Composite =============================================
	n = 8
	h = (b - a) / n

	Sim_approx = SimpsonRuleComposite(a, n, h)
	print('Simpsons Composite:', Sim_approx,'| Error:', abs_error_specific(Sim_approx))

	# Romberg Integration =============================================
	Rom_approx = R(4,4, a, b)
	print('Romberg:', Rom_approx,'| Error:', abs_error_specific(Rom_approx))

	# Guassian Quadrature ================================================
	n = 9
	Guass_approx = Guassian(a, b, n)
	print('Guassian:', Guass_approx,'| Error:', abs_error_specific(Guass_approx))

	# Nine Pt Newton Cotes ================================================
	Nine_NC_approx = NinePtNewtonCotes(a, b)
	print('Nine Pt Newton Cotes:', Nine_NC_approx,'| Error:', abs_error_specific(Nine_NC_approx))

# ====================================================
if __name__ == "__main__":
	main()

