import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import time

def J(z, lam, alpha):
	return z+(np.exp(-1j*2*alpha)*lam**2)/z

def circle(C, R):
	t = np.linspace(0, 2*np.pi, 200)
	return C+R*np.exp(1j*t)

def deg2radians(deg):
	return deg*np.pi/180

def flowlines(alpha, beta, V_inf, R, ratio):
	#alpha, beta are given in degrees
	#ratio =R/lam
	alpha = deg2radians(alpha)  # angle of attack
	# -beta is the argument of the complex no (Joukowski parameter - circle center)
	# beta = deg2radians(beta)
	beta = 0.07480469104343995
	if ratio <= 1:  # R/lam must be >1
		raise ValueError('R/lambda must be >1')
	lam = 1  # lam is the parameter of the Joukowski transformation

	center_c = np.exp(-1j*alpha)*(lam-R*np.exp(-1j*beta))
	# print(center_c)
	# exit()
	Circle = circle(center_c, R)
	# print(Circle)
	# plt.plot(Circle.real, Circle.imag)
	# plt.show()
	# exit()
	Airfoil = J(Circle, lam, alpha)
	X = np.arange(-3, 3, 0.1)
	Y = np.arange(-3, 3, 0.1)

	x, y = np.meshgrid(X, Y)
	z = x+1j*y
	XX = z-center_c
	# print(XX)
	# exit()
	R = 1
	z = ma.masked_where(np.absolute(XX) <= R, z)
	print(z[12])
	exit()
	w = J(z, lam, alpha)
	# print(w)
	# exit()
	beta = beta+alpha
	Z = z-center_c
	# print(Z.shape)
	# exit()
	Gamma = -4*np.pi*V_inf*R*np.sin(beta)  # circulation
	# print(Gamma)
	# exit()
	U = np.zeros(Z.shape, dtype=np.complex)
	with np.errstate(divide='ignore'):
		for m in range(Z.shape[0]):
			# due to this numpy bug https://github.com/numpy/numpy/issues/8516
			for n in range(Z.shape[1]):
									   #we evaluate  this term of the flow elementwise
				U[m, n] = Gamma*np.log((Z[m, n])/R)/(2*np.pi)
	# print(U)
	# exit()
	c_flow = V_inf*Z + (V_inf*R**2)/Z - 1j*U  # the complex flow
	# print(c_flow)
	# exit()
	return w, c_flow.imag, Airfoil

def main():
	alpha = 0
	beta = 5
	V_inf = 1
	R = 1
	ratio = 1.2

	levels = np.arange(-3, 3.7, 0.25).tolist()
	w, stream, Airfoil = flowlines(alpha, beta, V_inf, R, ratio)
	# plt.plot(Airfoil.real, Airfoil.imag)
	# plt.contour(w.real, w.imag, stream, levels=levels, colors='blue')
	# plt.show()

	# print("W:", w)
	# print("Stream:", stream)
	print("Airfoil:", Airfoil)
if __name__ == "__main__":
	main()
