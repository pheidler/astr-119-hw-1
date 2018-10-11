
import numpy as np

def main():
	i = 0	#int
	n = 10	#int
	x = 119.0	#float

	#numpy can declare arrays very quickly

	y = np.zeros(n,dtype=float) #declares 10 zeros

	for i in range(n):
		y[i] = 2.0 * float(i) + 1.0	#set y = 2i+1 as float

	for y_element in y:
		print(y_element)

if __name__== "__main__":
	main()

