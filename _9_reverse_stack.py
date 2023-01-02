from collections import deque

class Stack:
	def __init__(self):
		self.data = []

	def push(self, element):
		self.data.append(element)

	def pop(self):
		self.ele = self.data.pop()
		return self.ele

	# def peek(self):
	# 	return self.data[-1]

	def display(self):
		return self.data

	# def size(self):
	# 	print("No. of Elements in the stack:", len(self.data))

	def isEmpty(self):
		if len(self.data) == 0:
			return True
		else:
			return False

obj1 = Stack()

size = int(input("How many elements woud you like to add in the stack: "))
for i in range(size):
	element = int(input(f"Enter element {i+1}: "))
	obj1.push(element)


print("Original Stack:", obj1.display())

obj2 = Stack()
while obj1.isEmpty() != True:
	obj2.push(obj1.pop())

print("Reverse Stack:", obj2.display())