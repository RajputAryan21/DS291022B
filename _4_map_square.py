size = int(input("Enter the number of elements you want to add to the list: "))

lst = []
for i in range(size):
	ele = int(input(f"Enter element {i+1}: "))
	lst.append(ele)

def square(data):
	return data**2

print("\nOriginal List:", lst)
result = list(map(square, lst))
print("\nList after tripling the numbers :", result)