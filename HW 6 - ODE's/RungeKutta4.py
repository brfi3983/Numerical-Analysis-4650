import numpy as np
import math

# ====================================================
def f(t, w):
	return -t*w + 4*t/w

# ====================================================
def RungeKutta4(a, b, alp, N):
	w = alp
	h = (b - a) / N
	for i in range(0, N):
		t = a + i*h
		tp1 = a + (i+1)*h
		k1 = h*f(t,w)
		k2 = h*f(t + h/2, w + k1/2)
		k3 = h*f(t + h/2, w + k2/2)
		k4 = h*f(tp1, w + k3)
		w = w + 1/6*(k1 + 2*k2 + 2*k3 +k4)
	return w

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	approx = RungeKutta4(a, b, alpha, N)
	print(approx)

# ====================================================
if __name__ == "__main__":
	main()
