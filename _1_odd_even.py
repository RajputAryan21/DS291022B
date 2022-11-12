numbers = (15,786,37,98,1,69,4,20,21)
odd = 0
even = 0

for i in numbers:
	if i%2 == 0:
		even += 1
	else:
		odd += 1

print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)