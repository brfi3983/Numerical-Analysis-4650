<<<<<<< HEAD
import numpy as np
import math

# ====================================================
def f(t, w):
	return -t*w + 4*t/w

# ====================================================
def RungeKutta4(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + i*h
		tp1 = a + (i+1)*h
		k1 = h*f(t, w)
		k2 = h*f(t + h/2, w + k1/2)
		k3 = h*f(t + h/2, w + k2/2)
		k4 = h*f(tp1, w + k3)
		w = w + 1/6*(k1 + 2*k2 + 2*k3 + k4)
	return w

# ====================================================
def Midpoint(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		w = w + h*f(t + h/2, w + (h/2)*f(t, w))
	return w

# ====================================================
def ModifiedEuler(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		tp1 = a + h*(i + 1)
		w = w + (h/2)*(f(t, w) + f(tp1, w + h*f(t, w)))
	return w

# ====================================================
def Euler(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		w = alp + h*f(t, w)
	return w

# ====================================================
def h_array(num):
	h = np.zeros((num - 2,))
	for i in range(1, num - 1):
		h[i - 1] = (1/2**i)
	return h

# ====================================================
def ErrorStats(euler, mid, mod, rk4):
	true = 1.7018700527612773
	error_euler = abs(euler - true)
	error_mid = abs(mid - true)
	error_mod = abs(mod - true)
	error_rk4 = abs(rk4 - true)

	print('Euler: ', euler, ' || ', error_euler)
	print('Midpoint: ', mid, ' || ', error_mid)
	print('Modified Euler: ', mod, ' || ', error_mod)
	print('Runge-Kutta (Order 4): ', rk4, ' || ', error_rk4)

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	h_arr = h_array(N)
	for i in range(0, len(h_arr)):
		h = h_arr[i]
		print('-------------------------', '\nh value: ', h)
		euler = Euler(a, b, alpha, h)
		mid = Midpoint(a, b, alpha, h)
		mod = ModifiedEuler(a, b, alpha, h)
		RK4 = RungeKutta4(a, b, alpha, h)
		ErrorStats(euler, mid, mod, RK4)

# ====================================================
if __name__ == "__main__":
	main()
=======
import numpy as np
import math

# ====================================================
def f(t, w):
	return -t*w + 4*t/w

# ====================================================
def RungeKutta4(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + i*h
		tp1 = a + (i+1)*h
		k1 = h*f(t, w)
		k2 = h*f(t + h/2, w + k1/2)
		k3 = h*f(t + h/2, w + k2/2)
		k4 = h*f(tp1, w + k3)
		w = w + 1/6*(k1 + 2*k2 + 2*k3 + k4)
	return w

# ====================================================
def Midpoint(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		w = w + h*f(t + h/2, w + (h/2)*f(t, w))
	return w

# ====================================================
def ModifiedEuler(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		tp1 = a + h*(i + 1)
		w = w + (h/2)*(f(t, w) + f(tp1, w + h*f(t, w)))
	return w

# ====================================================
def Euler(a, b, alp, h):
	w = alp
	for i in range(0, int((b - a)/h)):
		t = a + h*i
		w = alp + h*f(t, w)
	return w

# ====================================================
def h_array(num):
	h = np.zeros((num - 2,))
	for i in range(1, num - 1):
		h[i - 1] = (1/2**i)
	return h

# ====================================================
def ErrorStats(euler, mid, mod, rk4):
	true = 1.7018700527612773
	error_euler = abs(euler - true)
	error_mid = abs(mid - true)
	error_mod = abs(mod - true)
	error_rk4 = abs(rk4 - true)

	print('Euler: ', euler, ' || ', error_euler)
	print('Midpoint: ', mid, ' || ', error_mid)
	print('Modified Euler: ', mod, ' || ', error_mod)
	print('Runge-Kutta (Order 4): ', rk4, ' || ', error_rk4)

# ====================================================
def main():
	a = 0
	b = 1
	alpha = 1
	N = 10

	h_arr = h_array(N)
	for i in range(0, len(h_arr)):
		h = h_arr[i]
		print('-------------------------', '\nh value: ', h)
		euler = Euler(a, b, alpha, h)
		mid = Midpoint(a, b, alpha, h)
		mod = ModifiedEuler(a, b, alpha, h)
		RK4 = RungeKutta4(a, b, alpha, h)
		ErrorStats(euler, mid, mod, RK4)

# ====================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
