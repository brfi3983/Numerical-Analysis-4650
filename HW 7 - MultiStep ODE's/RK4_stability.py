import numpy as np
import math

# ====================================================
def f(t, w):
	return -20*w

# ====================================================
def RungeKutta4(a, b, alp, h):
	w = alp
	N = int((b - a) / h)
	for i in range(0, N):
		t = a + i*h
		tp1 = a + (i+1)*h
		k1 = h*f(t, w)
		k2 = h*f(t + h/2, w + k1/2)
		k3 = h*f(t + h/2, w + k2/2)
		k4 = h*f(tp1, w + k3)
		w = w + 1/6*(k1 + 2*k2 + 2*k3 + k4)
	return w

# ====================================================
def main():
	a = 0
	b = 10
	alpha = 1
	h = 0
	for i in range(1, 100):
		h = h + (0.01)
		approx = RungeKutta4(a, b, alpha, h)
		print('h:', h, '|| approx:', approx)

# ====================================================
if __name__ == "__main__":
	main()
