import numpy as np

# ====================================================
# Integral you want to approximate
def f(x):
	return x*np.exp(2*x)

# ====================================================
def f_transform(y, a1, a2):
	x = a1 + a2*y

	return a2*f(x)

# ====================================================
def interval_transform(a, b):
	if (a == -1) & (b == 1):
		return 0, 1

	# Transforming interval to [-1, 1] via linear substitution
	a_arr = np.array([[1, -1], [1, 1]])
	b_vec = np.array([a, b])
	a1, a2 = np.linalg.solve(a_arr, b_vec)
	return a1, a2

# ====================================================
def LegrengeRoots(n):

	# Pulls roots from csv
	roots = np.genfromtxt("C:/Users/user/Documents/School/2019-2020/APPM 4650/Roots.csv", delimiter=",")
	roots[0][0] = 1
	nodes = np.zeros((n - 1))
	weights = np.zeros((n - 1))

	ind = -1
	for i in range(0, roots.shape[0]):
		if roots[i,0] == n:
			ind = i

	# Store it in a nodes and weights array
	nodes = roots[ind:ind + n,1]
	weights = roots[ind:ind + n,2]

	return nodes, weights

# ====================================================
def Guassian(nodes, weights, a1, a2):

	# Calculating the f value at the nodes
	f_arr = np.zeros((len(nodes)))
	for i in range(0, len(nodes)):
		f_arr[i] = f_transform(nodes[i], a1, a2)
	
	# Multiplying the f values by their weights for approx.
	I = np.dot(weights, f_arr)

	return I

# ====================================================
def main():
	# Interval and # pt. formula (n = 3 => 3 pt. guassian)
	a = 0
	b = 4
	n = 2

	# Transforming to [-1, 1] and grabbing weights/nodes
	a1, a2 = interval_transform(a,b)
	nodes, weights = LegrengeRoots(n)

	# Answer
	I = Guassian(nodes, weights, a1, a2)
	print(I)

# ====================================================
if __name__ == "__main__":
	main()
