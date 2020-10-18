import numpy as np
import math

# ====================================================
def f(t, w):
	return -t*w + 4*t/w

# ====================================================
def Euler(a, b, alp, N):
	h = (b - a) / N
	w = alp
	for i in range(0, N):
		t = a + h*i
		w = alp + h*f(t, w)
	return w

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	approx = Euler(a, b, alpha, N)

# ====================================================
if __name__ == "__main__":
	main()