import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

# Global variables (a = Joukouwski Paramter, alpha = angle of attack (radians), Vinf = velocity, lim = graphing bounds, levels = # contour lines)
alpha = 0 # radians
x0 = 0
y0 = 0.15

a = 1
Vinf = 1
lim = 3
levels = 50

# =========================================================================
def Circle(r, x0, y0):

	# Parameterize x, y in terms of t
	theta = np.linspace(0, 2*np.pi, 1000)

	# Get x, y arrays as theta varies
	x = r*np.cos(theta) + x0
	y = r*np.sin(theta) + y0

	z = x + 1j*y
	return z

# =========================================================================
def GraphBoth(C, A, f, F, Z, W, z0):
	# C = Cylinder, A = Airfoil, f = Cyinder, F = Airfoil Flow, Z = z-plane meshgrid, W = w-plane meshgrid (transformed from z)

	# changing axis to center circle
	delta = 0.85
	xmin = z0.real - lim*delta
	xmax = z0.real + lim*delta
	ymin = z0.imag - lim*delta
	ymax = z0.imag + lim*delta

	# Graphing Cylinder
	plt.subplot(1, 2, 1)
	plt.plot(C.real, C.imag)
	plt.contour(Z.real, Z.imag, f, levels)
	plt.grid()
	plt.title('Z Plane')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.axis([xmin, xmax, ymin, ymax])

	# Graphing Airfoil
	plt.subplot(1, 2, 2)
	plt.plot(A.real, A.imag)
	plt.contour(W.real, W.imag, F, levels)
	plt.grid()
	plt.title('W Plane')
	plt.xlabel('u')
	plt.ylabel('v')

	plt.show()

# =========================================================================
def CircleFlow(Z):
	# Stream Function for cylinder flow
	# Z = Z*np.exp(-1j*alpha)

	f = Z.imag - Z.imag/(Z.real**2 + Z.imag**2)
	return f

# =========================================================================
def Circle2Aifoil(R, x0, y0):

	# Cylinder and Airfoil Geometry
	cylinder = Circle(R, x0, y0)
	airfoil = Transformation(cylinder)

	# Calculating angle off real axis to center of circle
	beta = np.arctan(y0/(a-x0))

	# Creating Meshgrid
	x_rec = np.arange(-lim,lim,0.1)
	y_rec = np.arange(-lim,lim,0.1)
	X, Y = np.meshgrid((x_rec), (y_rec))
	Z = X + 1j*Y

	# Removing(masking) values that are within the body
	z0 = x0 + 1j*y0
	Z = np.ma.masked_where(np.absolute(Z - z0) <= R, Z)

	# Meshgrid values for the Z and W plane
	Z = Z
	W = Transformation(Z)
	
	#alpha is 0 right now
	gamma = -4*np.pi*Vinf*R*np.sin(beta + alpha)

	# Calculuting the Vortex Flow (ignoring values that were masked above)
	U = np.zeros(Z.shape, dtype=np.complex)
	with np.errstate(divide='ignore'):
		for m in range(Z.shape[0]):
			for n in range(Z.shape[1]):
				U[m, n] = gamma*np.log((Z[m, n])/R)/(2*np.pi)

	# Cylinder flow and Airfoil Flow
	airfoil_complex_potential = (Vinf*Z + (Vinf*R**2)/Z - 1j*U)
	f = CircleFlow(Z)
	F = airfoil_complex_potential.imag

	# Graphing both geometries and their flowlines
	GraphBoth(cylinder, airfoil, f, F, Z, W, z0)


def Transformation(z):

	# Joukowski Transformation (if you assume non-zero real angle then do Karman-Trefftz)
	ang_att = np.exp(-2j*alpha)
	# ang_att = 1
	n = 1
	J = (z + ang_att*a**2/z)
	Jx = (n*z - n*ang_att*a**2/z)
	lam = 0.16
	J1 = J + lam*J**2
	J2 = np.exp(J)

	return np.array(Jx, dtype=complex)

# =========================================================================
def main():

	# Setting Parameters for Initial Circle (Note: x0 <= 0 in order to work)
	r = np.sqrt((a-x0)**2 + y0**2)

	# Everything else
	Circle2Aifoil(r, x0, y0)

# =========================================================================
if __name__ == "__main__":
	main()
