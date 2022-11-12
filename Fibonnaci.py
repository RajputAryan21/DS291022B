count = 0
num1 = 0
num2 = 1
while count<50:
	seq = num1 + num2
	print(seq, end = " ")
	num1 = num2
	num2 = seq
	count += 1 