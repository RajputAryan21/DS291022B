class Array:
	def __init__(self,size):
		self.size = size
		self.data = []
		self.length = 0

	def display(self):
		if self.length <= self.size:
			return self.data

	def add(self, element):
		self.data.append(element)

	def insert_at(self,index, element):
		self.data.insert(index, element)

	def reverse(self):
		for i in range(len(self.data)):
			self.insert_at(i,self.data[-1])
			self.data.pop()


size = int(input("Enter the size of Array: "))
array = Array(size)
for i in range(size):
    ele = int(input(f"Enter the {i+1} element: "))
    array.add(ele)
print("Original Array:", array.display())
array.reverse()
print("Reverse Array:", array.display())