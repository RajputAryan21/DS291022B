class Point:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z 

	def sqSum(self):
		self.x = self.x**2
		self.y = self.y**2
		self.z = self.z**2
		return self.x+self.y+self.z

x,y,z = input("Enter three numbers: ").split()

point = Point(int(x),int(y),int(z))
result = point.sqSum()
print("Result:", result)