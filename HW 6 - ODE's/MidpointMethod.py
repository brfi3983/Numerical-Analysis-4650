<<<<<<< HEAD
import numpy as np
import math

# ====================================================
def f(t,w):
	return -t*w + 4*t/w

# ====================================================
def Midpoint(a, b, alp, N):
	w = alp
	h = (b - a)/N
	for i in range(0, N):
		t = a + h*i
		w = w + h*f(t + h/2, w + (h/2)*f(t,w))
	return w

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	approx = Midpoint(a, b, alpha, N)

# ====================================================
if __name__ == "__main__":
	main()
=======
import numpy as np
import math

# ====================================================
def f(t,w):
	return -t*w + 4*t/w

# ====================================================
def Midpoint(a, b, alp, N):
	w = alp
	h = (b - a)/N
	for i in range(0, N):
		t = a + h*i
		w = w + h*f(t + h/2, w + (h/2)*f(t,w))
	return w

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	approx = Midpoint(a, b, alpha, N)

# ====================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
