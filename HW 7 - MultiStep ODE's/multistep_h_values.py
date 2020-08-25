import numpy as np
import matplotlib.pyplot as plt
import math

# ====================================================
def Method(a, b, alp, h):

	# Finding total number of iterations in [a,b]
	N = int((b - a) / h)

	# Initial Condidtions
	w = alp
	w1 = 1 - math.exp(-h)

	# Using difference iteration method
	w_arr = np.zeros((N + 1))
	t_arr = np.zeros((N + 1))

	w_arr[0] = w
	w_arr[1] = w1
	t_arr[0] = a
	t_arr[1] = a + h
	for i in range(0, N - 1):
		w2 = 4*w1 -3*w - 2*h*(1 - w)
		w_arr[i + 2] = w2
		t_arr[i + 2] = t_arr[i + 1] + h
		w = w1
		w1 = w2
	return w2, w_arr, t_arr

# ====================================================
def true_func(t):
	x = np.zeros((len(t)))
	for i in range(0, len(x)):
		x[i] = -math.exp(-t[i]) + 1
	return x

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 0
	h = 0.1
	approx, w_arr, t_arr = Method(a, b, alpha, h)
	h = 0.01
	approx2, w_arr2, t_arr2 = Method(a, b, alpha, h)
	true_arr = true_func(t_arr)

	plt.plot(t_arr, w_arr, label='h=0.1')
	plt.plot(t_arr, true_arr, label='true')
	plt.plot(t_arr2, w_arr2, label='h=0.01')
	plt.legend()
	plt.show()

# ====================================================
if __name__ == "__main__":
	main()
