<<<<<<< HEAD
import numpy as np
import math

# PLEASE TELL ME THERE IS A BETTER WAY TO DO THIS!
# ====================================================
# ====================================================
def f1(t, u1, u2, u3):
	return u1 + 2*u2 - 2*u3 + math.exp(-t)
def f2(t, u1, u2, u3):
	return u2 + u3 - 2*math.exp(-t)
def f3(t, u1, u2, u3):
	return u1 + 2*u2 + math.exp(-t)

# ====================================================
# ====================================================
def k11 (h, t, u1, u2, u3):
	return h*f1(t, u1, u2, u3)
def k12 (h, t, u1, u2, u3):
	return h*f2(t, u1, u2, u3)
def k13 (h, t, u1, u2, u3):
	return h*f3(t, u1, u2, u3)

# ====================================================
# ====================================================
def k21 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f1(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)
def k22 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f2(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)
def k23 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f3(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)

# ====================================================
# ====================================================
def k31 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f1(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)
def k32 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f2(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)
def k33 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f3(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)

# ====================================================
# ====================================================
def k41 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f1(t + h, u1 + k31x, u2 + k32x, u3 + k33x)
def k42 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f2(t + h, u1 + k31x, u2 + k32x, u3 + k33x)
def k43 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f3(t + h, u1 + k31x, u2 + k32x, u3 + k33x)

# ====================================================
# ====================================================
def w1 (u1, k11x, k21x, k31x, k41x):
	return u1 + (1/6)*(k11x + 2*k21x + 2*k31x + k41x)
def w2 (u2, k12x, k22x, k32x, k42x):
	return u2 + (1/6)*(k12x + 2*k22x + 2*k32x + k42x)
def w3 (u3, k13x, k23x, k33x, k43x):
	return u3 + (1/6)*(k13x + 2*k23x + 2*k33x + k43x)

# ====================================================
# ====================================================
def u1_true(t):
	return -3*math.exp(-t) - 3*math.sin(t) + 6*math.cos(t)
def u2_true(t):
	return 3*math.exp(-t)/2 + 0.3*math.sin(t) - 2.1*math.cos(t) - 0.4*math.exp(2*t)
def u3_true(t):
	return -math.exp(-t) +12*math.cos(t)/5 + 9*math.sin(t)/5 - 2*math.exp(2*t)/5

# ====================================================
# ====================================================
def Error(u1, u2, u3):
	return abs(u1 - u1_true(1)), abs(u2 - u2_true(1)), abs(u3 - u3_true(1))

# ====================================================
def RK4_Systems3(u1, u2, u3, a, b, h):
	N = int((b - a) / h)
	for i in range(0, N):
		t = a + i*h

		k11x = k11(h, t, u1, u2, u3)
		k12x = k12(h, t, u1, u2, u3)
		k13x = k13(h, t, u1, u2, u3)

		k21x = k21(t, h, u1, k11x, u2, k12x, u3, k13x)
		k22x = k22(t, h, u1, k11x, u2, k12x, u3, k13x)
		k23x = k23(t, h, u1, k11x, u2, k12x, u3, k13x)

		k31x = k31(t, h, u1, k21x, u2, k22x, u3, k23x)
		k32x = k32(t, h, u1, k21x, u2, k22x, u3, k23x)
		k33x = k33(t, h, u1, k21x, u2, k22x, u3, k23x)

		k41x = k41(t, h, u1, k31x, u2, k32x, u3, k33x)
		k42x = k42(t, h, u1, k31x, u2, k32x, u3, k33x)
		k43x = k43(t, h, u1, k31x, u2, k32x, u3, k33x)

		u1 = w1(u1, k11x, k21x, k31x, k41x)
		u2 = w2(u2, k12x, k22x, k32x, k42x)
		u3 = w3(u3, k13x, k23x, k33x, k43x)

	return u1, u2, u3

# ====================================================
def main():
	a = 0
	b = 1
	u1 = 3
	u2 = -1
	u3 = 1
	h = 0.1

	w1, w2, w3 = RK4_Systems3(u1, u2, u3, a, b, h)
	e1, e2, e3 = Error(w1, w2, w3)
	print('Pred u1:', w1, '|| Error:', e1)
	print('Pred u2:', w2, '|| Error:', e2)
	print('Pred u3:', w3, '|| Error:', e3)

# ====================================================
if __name__ == "__main__":
	main()
=======
import numpy as np
import math

# PLEASE TELL ME THERE IS A BETTER WAY TO DO THIS!
# ====================================================
# ====================================================
def f1(t, u1, u2, u3):
	return u1 + 2*u2 - 2*u3 + math.exp(-t)
def f2(t, u1, u2, u3):
	return u2 + u3 - 2*math.exp(-t)
def f3(t, u1, u2, u3):
	return u1 + 2*u2 + math.exp(-t)

# ====================================================
# ====================================================
def k11 (h, t, u1, u2, u3):
	return h*f1(t, u1, u2, u3)
def k12 (h, t, u1, u2, u3):
	return h*f2(t, u1, u2, u3)
def k13 (h, t, u1, u2, u3):
	return h*f3(t, u1, u2, u3)

# ====================================================
# ====================================================
def k21 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f1(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)
def k22 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f2(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)
def k23 (t, h, u1, k11x, u2, k12x, u3, k13x):
	return h*f3(t + h/2, u1 + k11x/2, u2 + k12x/2, u3 + k13x/2)

# ====================================================
# ====================================================
def k31 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f1(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)
def k32 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f2(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)
def k33 (t, h, u1, k21x, u2, k22x, u3, k23x):
	return h*f3(t + h/2, u1 + k21x/2, u2 + k22x/2, u3 + k23x/2)

# ====================================================
# ====================================================
def k41 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f1(t + h, u1 + k31x, u2 + k32x, u3 + k33x)
def k42 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f2(t + h, u1 + k31x, u2 + k32x, u3 + k33x)
def k43 (t, h, u1, k31x, u2, k32x, u3, k33x):
	return h*f3(t + h, u1 + k31x, u2 + k32x, u3 + k33x)

# ====================================================
# ====================================================
def w1 (u1, k11x, k21x, k31x, k41x):
	return u1 + (1/6)*(k11x + 2*k21x + 2*k31x + k41x)
def w2 (u2, k12x, k22x, k32x, k42x):
	return u2 + (1/6)*(k12x + 2*k22x + 2*k32x + k42x)
def w3 (u3, k13x, k23x, k33x, k43x):
	return u3 + (1/6)*(k13x + 2*k23x + 2*k33x + k43x)

# ====================================================
# ====================================================
def u1_true(t):
	return -3*math.exp(-t) - 3*math.sin(t) + 6*math.cos(t)
def u2_true(t):
	return 3*math.exp(-t)/2 + 0.3*math.sin(t) - 2.1*math.cos(t) - 0.4*math.exp(2*t)
def u3_true(t):
	return -math.exp(-t) +12*math.cos(t)/5 + 9*math.sin(t)/5 - 2*math.exp(2*t)/5

# ====================================================
# ====================================================
def Error(u1, u2, u3):
	return abs(u1 - u1_true(1)), abs(u2 - u2_true(1)), abs(u3 - u3_true(1))

# ====================================================
def RK4_Systems3(u1, u2, u3, a, b, h):
	N = int((b - a) / h)
	for i in range(0, N):
		t = a + i*h

		k11x = k11(h, t, u1, u2, u3)
		k12x = k12(h, t, u1, u2, u3)
		k13x = k13(h, t, u1, u2, u3)

		k21x = k21(t, h, u1, k11x, u2, k12x, u3, k13x)
		k22x = k22(t, h, u1, k11x, u2, k12x, u3, k13x)
		k23x = k23(t, h, u1, k11x, u2, k12x, u3, k13x)

		k31x = k31(t, h, u1, k21x, u2, k22x, u3, k23x)
		k32x = k32(t, h, u1, k21x, u2, k22x, u3, k23x)
		k33x = k33(t, h, u1, k21x, u2, k22x, u3, k23x)

		k41x = k41(t, h, u1, k31x, u2, k32x, u3, k33x)
		k42x = k42(t, h, u1, k31x, u2, k32x, u3, k33x)
		k43x = k43(t, h, u1, k31x, u2, k32x, u3, k33x)

		u1 = w1(u1, k11x, k21x, k31x, k41x)
		u2 = w2(u2, k12x, k22x, k32x, k42x)
		u3 = w3(u3, k13x, k23x, k33x, k43x)

	return u1, u2, u3

# ====================================================
def main():
	a = 0
	b = 1
	u1 = 3
	u2 = -1
	u3 = 1
	h = 0.1

	w1, w2, w3 = RK4_Systems3(u1, u2, u3, a, b, h)
	e1, e2, e3 = Error(w1, w2, w3)
	print('Pred u1:', w1, '|| Error:', e1)
	print('Pred u2:', w2, '|| Error:', e2)
	print('Pred u3:', w3, '|| Error:', e3)

# ====================================================
if __name__ == "__main__":
	main()
>>>>>>> df807cb4c3d48e521e288700e6b4420d69ede4c5
