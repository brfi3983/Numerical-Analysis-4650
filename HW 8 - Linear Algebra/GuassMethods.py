import numpy as np

def GuassJacobi(A, b, G, true):

	temp = np.zeros((A.shape[0]), dtype = float)
	g = np.copy(G)
	count = 0
	error_x = 0
	while error_x == 0:
		for i in range(0, A.shape[0]):
			s = customDot(A[i,:], g, i)
			temp[i] = (1/A[i][i])*(b[i] - s)
		count += 1
		g = np.copy(temp)
		print('X_' + str(count) + ':', g)
		error_x = error(g, true)
	return g, count

def GuassSeidel(A, b, G, true):

	g = np.copy(G)
	count = 0
	error_x = 0
	while error_x == 0:
		for i in range(0, A.shape[0]):
			s = customDot(A[i, :], g, i)
			g[i] = (1/A[i][i])*(b[i] - s)
		count += 1
		print('X_' + str(count) + ':', g)
		error_x = error(g, true)
	return g, count

def SOR(A, b, G, w, true):

	g = np.copy(G)
	count = 0
	error_x = 0
	while error_x == 0:
		for i in range(0, A.shape[0]):
			s = customDot(A[i, :], g, i)
			g[i] = w*(1/A[i][i])*(b[i] - s) + g[i]*(1 - w)
		count += 1
		print('X_' + str(count) + ':', g)
		error_x = error(g, true)
	return g, count

def customDot(a, g, k):
	s = 0
	for i in range(0, a.shape[0]):
		if i != k:
			s += a[i]*g[i]

	return s
def error(pred, true):
	valid = 1
	for i in range(0, pred.shape[0]):
		if abs(pred[i] - true[i]) > 10e-8:
			return 0
	return valid
def main():
	# Problem to Solve

	A = np.array([ \
		[4, -1, 0, -1, 0, 0], \
		[-1, 4, -1, 0, -1, 0], \
		[0, -1, 4, 0, 0, -1], \
		[-1, 0, 0, 4, -1, 0], \
		[0, -1, 0, -1, 4, -1], \
		[0, 0, -1, 0, -1, 4]])
	b = np.array([2, 1, 2, 2, 1, 2]).T
	x0 = np.array([0, 0, 0, 0, 0, 0], dtype=float)
	true = np.ones((6, 1))

	# Using Jacobi, Seidel, and SOR
	print('\nJacobi:')
	test, count = GuassJacobi(A, b, x0, true)
	print('Iterations:', count)

	print('\nSeidel:')
	test, count = GuassSeidel(A, b, x0, true)
	print('Iterations:', count)

	w = 1.113
	print('\nSOR:')
	test, count = SOR(A, b, x0, w, true)
	print('Iterations:', count)
if __name__ == "__main__":
	main()