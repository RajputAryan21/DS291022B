size = int(input("Enter the number of elements you want to add to the list: "))

lst = []
for i in range(size):
	ele = int(input(f"Enter element {i+1}: "))
	lst.append(ele)

def add(data):
	return data*3

print("\nOriginal List:", lst)
result = list(map(add, lst))
print("\nList after tripling the numbers :", result)