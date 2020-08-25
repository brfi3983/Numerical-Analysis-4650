<<<<<<< HEAD
import numpy as np
import math

# ====================================================
def getInitalVals(a, h):
	return [f(a + 3*h), f(a + 2*h), f(a + h), f(a)]

# ====================================================
def f(t):
	return -1 + math.log(2 - math.exp(1 - math.exp(t)))

# ====================================================
def f_p(t, y):
	return math.exp(t)*(2*math.exp(-1*(y+1)) - 1)

# ====================================================
def AdamsB(h, temp_arr, t):
	w3, w2, w1, w0 = temp_arr

	return w3 + (h/24)*(55*f_p(t + 3*h, w3) - 59*f_p(t + 2*h, w2) +
                     37*f_p(t + h, w1) - 9*f_p(t, w0))

# ====================================================
def AdamsM(h, temp_arr, t):
	wp, w3, w2, w1 = temp_arr
	return w3 + (h/24)*(9*f_p(t + 4*h, wp) + 19*f_p(t + 3*h, w3)
                     - 5*f_p(t + 2*h, w2) + f_p(t + h, w1))

# ====================================================
def TrueV(a):
	return f(a)

# ====================================================
def Error(true, pred):
	return abs(pred - true)

# ====================================================
def AdamsPredCorr(a, b, h, p_arr):
	n = int((b - h*3)/h)
	temp_arr = np.zeros((len(p_arr)))
	temp_arr = p_arr
	for i in range(0, n + 1):
		t = h*i
		wp = AdamsB(h, temp_arr, t)
		temp_arr = np.roll(temp_arr, 1)
		temp_arr[0] = wp
		w = AdamsM(h, temp_arr, t)
	return w

# ====================================================
def get_h_arr():
	h_arr = np.zeros((7))
	for i in range(3, 10):
		h_arr[i - 3] = 1/2**i
	return h_arr

# ====================================================
def main():
	a = 0
	b = 1
	h_arr = get_h_arr()
	true = TrueV(b)
	for i in range(0, len(h_arr)):
		h = h_arr[i]
		InitVals = getInitalVals(a, h)
		w = AdamsPredCorr(a, b, h, InitVals)
		error = Error(true, w)
		print('h:', h, '|| Predicted:', w, '|| Error:', error)

# ====================================================
if __name__ == "__main__":
	main()
=======
import numpy as np
import math

# ====================================================
def getInitalVals(a, h):
	return [f(a + 3*h), f(a + 2*h), f(a + h), f(a)]

# ====================================================
def f(t):
	return -1 + math.log(2 - math.exp(1 - math.exp(t)))

# ====================================================
def f_p(t, y):
	return math.exp(t)*(2*math.exp(-1*(y+1)) - 1)

# ====================================================
def AdamsB(h, temp_arr, t):
	w3, w2, w1, w0 = temp_arr

	return w3 + (h/24)*(55*f_p(t + 3*h, w3) - 59*f_p(t + 2*h, w2) +
                     37*f_p(t + h, w1) - 9*f_p(t, w0))

# ====================================================
def AdamsM(h, temp_arr, t):
	wp, w3, w2, w1 = temp_arr
	return w3 + (h/24)*(9*f_p(t + 4*h, wp) + 19*f_p(t + 3*h, w3)
                     - 5*f_p(t + 2*h, w2) + f_p(t + h, w1))

# ====================================================
def TrueV(a):
	return f(a)

# ====================================================
def Error(true, pred):
	return abs(pred - true)

# ====================================================
def AdamsPredCorr(a, b, h, p_arr):
	n = int((b - h*3)/h)
	temp_arr = np.zeros((len(p_arr)))
	temp_arr = p_arr
	for i in range(0, n + 1):
		t = h*i
		wp = AdamsB(h, temp_arr, t)
		temp_arr = np.roll(temp_arr, 1)
		temp_arr[0] = wp
		w = AdamsM(h, temp_arr, t)
	return w

# ====================================================
def get_h_arr():
	h_arr = np.zeros((7))
	for i in range(3, 10):
		h_arr[i - 3] = 1/2**i
	return h_arr

# ====================================================
def main():
	a = 0
	b = 1
	h_arr = get_h_arr()
	true = TrueV(b)
	for i in range(0, len(h_arr)):
		h = h_arr[i]
		InitVals = getInitalVals(a, h)
		w = AdamsPredCorr(a, b, h, InitVals)
		error = Error(true, w)
		print('h:', h, '|| Predicted:', w, '|| Error:', error)

# ====================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
