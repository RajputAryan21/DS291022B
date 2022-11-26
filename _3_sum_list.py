lst = []
size = int(input("How many elements would you like to add in the list? "))

for i in range(size):
	ele = int(input(f"Enter element no. {i+1}: "))
	lst.append(ele)

sum = 0
for i in lst:
	sum += i

print("The sum of the numbers in the list:", sum)