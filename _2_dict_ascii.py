ascii_dict = {}

for i in range(97, 123):
	char = chr(i)
	ascii_dict[char] = i

print("Dictionary of alphabets with their ASCII values: ", ascii_dict)