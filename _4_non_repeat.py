string = input("Enter a string: ").lower()

def find(string):
	for i in range(len(string)):
		count = 0
		for j in range(len(string)):
			if string[i] == string[j]:
				count += 1
		if count == 1:
			return string[i]

result = find(string)
print("First non-repeated character:", result)