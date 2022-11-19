lst = []

size = int(input("Enter the number of tuples you want to add in the list: "))

for i in range(size):
	num = tuple(input(f"Enter the values for the {i+1} tuple: ").split(' '))
	lst.append(num)

print("List of tuples: ", lst)

for i in range(len(lst)):
	for j in range(i, len(lst)):
		if lst[i][1] > lst[j][1]:
			lst[i], lst[j] = lst[j], lst[i]

print("Sorted list: ", lst)