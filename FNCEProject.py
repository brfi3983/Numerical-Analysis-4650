import numpy as np

def main():
	A = np.array([1.0000, 0.2095, 0.5265, 0.2375, 0.2981, 1.3258, 1.6613]).reshape(7, 1)
	B = np.matmul(A, A.T)
	V = np.array([0.0145, 0.0276, 0.0371, 0.0219, 0.0184, 0.0648, 0.0884])
	# ANS = np.multiply(B, V[])
	ANS = 0.145*B
	print(A)
	print(V)
	print(ANS)
	# D = np.zeros((A.shape[0], A.shape[0]))
	# for i in range(0, variances.shape[0]):
	# 	D[i][i] = variances[i]
	# C = np.ones((3,3))
	# D = np.array([3, np.pi, 99]).reshape(3, 1)
	# print(D.shape)
	# X = np.multiply(C,D)
	# print(C, D, X)
if __name__ == "__main__":
	main()
