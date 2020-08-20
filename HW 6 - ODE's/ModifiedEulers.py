import numpy as np
import math

# ====================================================
def f(t, w):
	return -t*w + 4*t/w

# ====================================================
def ModifiedEuler(a, b, alp, N):
	w = alp
	h = (b - a)/N
	for i in range(0, N):
		t = a + h*i
		tp1 = a + h*(i + 1)
		w = w + (h/2)*(f(t,w) + f(tp1, w + h*f(t,w)))
	return w

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	approx = ModifiedEuler(a, b, alpha, N)

# ====================================================
if __name__ == "__main__":
	main()
