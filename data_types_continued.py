s = "I am a string."
print(type(s))

yes = True
print(type(yes))  #str

no = False
print(type(no))

alpha_list = ["a","b","c"] #initialization
print(type(alpha_list))  #tuple
print(type(alpha_list[0]))	#string
alpha_list.append("d")	#adds
print(alpha_list)	

 #tuples are ordered and unchangeable
alpha_tuple = ("a","b","c")  #initialized with parentheses
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't add elements to tuples!")
print(alpha_tuple)
