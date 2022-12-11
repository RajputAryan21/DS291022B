class Student:
	
	def setName(self, __name):
		self.__name = __name

	def getName(self):
		return self.__name

	def setRollNumber(self, __rollNumber):
		self.__rollNumber = __rollNumber

	def getRollNumber(self):
		return self.__rollNumber

student = Student()

name = input("Enter Student Name: ")
student.setName(name)

rno = int(input("Enter Student Roll Number: "))
student.setRollNumber(rno)

print("Student Name:", student.getName())
print("Student Roll Number:", student.getRollNumber())