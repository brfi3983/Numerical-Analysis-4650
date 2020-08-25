<<<<<<< HEAD
import numpy as np
import math

# ====================================================
def f(x):
	return (math.cos(2*x) + math.exp(x**2) + 3) / (4 + math.sin(4*x))

# ====================================================
def NinePtNewtonCotes(x_0, x_8):
	h = (x_8 - x_0) / 9
	I = (4*h/14175)*(989*f(x_0) + 5888*f(x_0 + h) -928 *
              f(x_0 + 2*h) + 10496*f(x_0 + 3*h) - 4540*f(x_0 + 4*h) + \
				   10496*f(x_0 + 5*h) - 928*f(x_0 + 6*h) + 5888*f(x_0 + 7*h) + 989*f(x_0 + 8*h))
	return I

# ====================================================
def main():
	a = -1
	b = 1
	I = NinePtNewtonCotes(a, b)
	print(I)

# ====================================================
if __name__ == "__main__":
	main()
=======
import numpy as np
import math

# ====================================================
def f(x):
	return (math.cos(2*x) + math.exp(x**2) + 3) / (4 + math.sin(4*x))

# ====================================================
def NinePtNewtonCotes(x_0, x_8):
	h = (x_8 - x_0) / 9
	I = (4*h/14175)*(989*f(x_0) + 5888*f(x_0 + h) -928 *
              f(x_0 + 2*h) + 10496*f(x_0 + 3*h) - 4540*f(x_0 + 4*h) + \
				   10496*f(x_0 + 5*h) - 928*f(x_0 + 6*h) + 5888*f(x_0 + 7*h) + 989*f(x_0 + 8*h))
	return I

# ====================================================
def main():
	a = -1
	b = 1
	I = NinePtNewtonCotes(a, b)
	print(I)

# ====================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
