import numpy as np
import sympy as sym

def main():
	x = sym.Symbol('x')
	y = sym.Symbol('y')
	
	x0 = sym.Symbol('x0')
	y0 = sym.Symbol('y0')

	f = (x - x0) + 1j*(y - y0) + 1/((x - x0) + 1j*(y - y0))
	x0 = 0
	print(sym.re(f))
	# print(sym.im(f))
if __name__ == "__main__":
	main()
