class Stack:
	def __init__(self):
		self.data = []

	def display(self):
		return self.data
		
	def push(self, element):
		self.data.append(element)

	def peek(self):
		return self.data[-1]

	def find(self):
		min = self.data[0]
		for i in self.data:
			if i < min:
				min = i
		return min

stack = Stack()

size = int(input("How many elements woud you like to add in the stack: "))
for i in range(size):
	element = int(input(f"Enter element {i+1}: "))
	stack.push(element)

print("Stack:", stack.display())
print("Smallest number in the stack:", stack.find())