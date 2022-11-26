string = input("Enter a string: ")

upper = 0
lower = 0
for i in string:
	if i.isupper():
		upper += 1 
	elif i.islower():
		lower += 1
	
print("The number of upper case letters in the string:", upper)
print("The number of lower case letters in the string:", lower)