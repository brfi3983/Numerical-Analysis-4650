import numpy as np
import matplotlib.pyplot as plt
import math

# ====================================================
def f(t, w):
	return y

# ====================================================
def true_f(t):
	return math.exp(t)

# ====================================================
def Euler(a, b, alp, h):
	w_arr = np.zeros((int((b - a)/h)))
	w_arr[0] = alp
	for i in range(1, int((b - a)/h)):
		t = a + i*h
		w_arr[i] = w_arr[i - 1] + h*t
	return w_arr

# ====================================================
def Taylor2(a, b, alp, h):
	w_arr = np.zeros((int((b - a)/h)))
	w_arr[0] = alp
	for i in range(1, int((b - a)/h)):
		w_arr[i] = (h + 1)*w_arr[i - 1]
	return w_arr

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	h = 1/4
	x = np.linspace(0, 1, int((b-a)/h))
	euler = Euler(a, b, alpha, h)
	tay2 = Taylor2(a, b, alpha, h)
	y = np.zeros((len(x)))
	for i in range(0, len(x)):
		y[i] = true_f(x[i])
	plt.plot(x, euler, label='Euler')
	plt.plot(x, tay2, label='Taylor')
	plt.plot(x, y, label='True')
	plt.legend()

	error_euler = abs(euler[-1] - true_f(1))
	error_tay = abs(tay2[-1] - true_f(1))
	print('Euler Error:', error_euler)
	print('Taylor Error:', error_tay)

	plt.show()

# ====================================================
if __name__ == "__main__":
	main()