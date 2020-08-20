def floatNum(s, c, f):
	return (-1)**s*2**(c - 1023)*(1 + f)

# ================================================
def SmallestFloating():
	# Define constants and generally low float number
	i = 9
	num = floatNum(0, 1, i)

	# Iterate (and decrease the float value) until you can not decrease the float number by any more. Then return the value.
	while i >= -1:
		temp = num
		num = floatNum(0, 1, i)
		i -= 1
		if num == 0:
			return temp

# =================================================
def LargestFloating():

	# Define constants and generally high float number
	i = 30
	num = floatNum(0, 2046, 1 - 2**(-52))

	# Iterate (and increase the float value) until you can not increase the float number by any more. Then return the value.
	while i > 0:
		temp = num
		num = floatNum(0, 2046, 1 - 2**(-i))
		i += 1
		if num == float('Inf'):
			return temp

# =================================================
def machineEpsilon():

	# Constants
	epsilon = 1
	count = 0
	
	# Shift our epsilon value one bit over (by dividing by 2) at a time until it can no longer be reduced
	while (1 + epsilon / 2 > 1):
		epsilon = epsilon / 2
		count = count + 1

	# Return epsilon and count size
	return epsilon, count

# ==================================================
def main():
	# Use Functions to find largest and smallest floating point number along with macine epsilon

	x = SmallestFloating()
	y = LargestFloating()
	z, count = machineEpsilon()
	print("Smallest Floating:", x,"\nLargest Floating:", y,"\nMachine Epsilon:", z)

# ==================================================
if __name__ == "__main__":
	main()
