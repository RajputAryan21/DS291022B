word = input("Enter a word: ")
i = len(word)

print("Output: ", end="")
while i>0:
	print(word[i-1], end="")
	i -= 1