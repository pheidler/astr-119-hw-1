import numpy as np 

i = 10  #integer
print(type(i)) #prints type

a_i = np.zeros(i,dtype=int) #declares array of ints
print(type(a_i))   #returns ndarray
print(type(a_i[0]))	#returns int64

x = 119.0	#float
print(type(x))	#prints type

y = 1.19e2	#float
print(type(y))	#prints type

z = np.zeros(i,dtype=float) #declares array of floats
print(type(z))   #returns ndarray
print(type(z[0]))	#returns float64