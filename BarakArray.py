import numpy as np

def RangeN(n):
	arr = np.zeros((10*n + 1))
	init = 1
	step = init/10
	arr[0] = init
	for i in range(1, 10*n):
		if (i + 1) % 10 == 0:
			# print(i, arr[i])
			init = arr[i]
			step = init/10
			# print(step)
		# print(step)
		arr[i] = arr[i - 1] - step
		print(i, arr[i])
	# print(arr)
	return arr
def main():
	n = 3
	x = RangeN(n)
	print('ARRAY:', x)
if __name__ == "__main__":
	main()
