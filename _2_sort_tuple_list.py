lst = [(1,2), (3,1), (5,3), (7,5), (9,4), (3,3)]
print("List of tuples: ", lst)

for i in range(len(lst)):
	for j in range(i, len(lst)):
		if lst[i][1] > lst[j][1]:
			lst[i], lst[j] = lst[j], lst[i]

print("Sorted list: ", lst)