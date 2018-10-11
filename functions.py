import numpy as np 
import sys

def expo(x):
	return np.exp(x)  #return e^x 


def show_expo(n):
	for i in range(n):
		print(expo(float(i)))  #prints out e^i for numbers n


def main():
	n = 10 

	if(len(sys.argv)> 1):
		n = int(sys.argv[1])  #checks if a command line argument has been provided, uses it

	show_expo(n)

if __name__ == "__main__":
	main()
