class Dog:
	def __init__(self,name,age,coat_color):
		self.name = name
		self.age = age
		self.coat_color = coat_color

	def description(self):
		print(f"Name: {self.name} \nAge: {self.age}")

	def get_info(self):
		print(f"Coat Color: {self.coat_color}")

class JackRussellTerrier(Dog):
	def __init__(self,name,age,coat_color):
		super().__init__(name,age,coat_color)
	
	def description(self):
		super().description()
	
	def get_info(self):
		super().get_info()

	def gender(self, gender):
		print(f"Gender: {gender}")

	def owner(self,name):
		print(f"Owner's Name: {name}")


class Bulldog(Dog):
	def __init__(self,name,age,coat_color):
		super().__init__(name,age,coat_color)

	def description(self):
		super().description()

	def get_info(self):
		super().get_info()

	def gender(self, gender):
		print(f"Gender: {gender}")

	def owner(self,name):
		print(f"Owner's Name: {name}")
		

dog =Dog("Coco",6,"Brown")
print("--Parent class--")
dog.description()
dog.get_info()

obj1 = JackRussellTerrier("Jack",7,"Black")
print("--Child class JackRussellTerrier--")
obj1.description()
obj1.get_info()
obj1.gender("Male")
obj1.owner("Rahul")

obj2 = Bulldog("Tyson",5,"Grey")
print("--Child class Bulldog--")
obj2.description()
obj2.get_info()
obj2.gender("Male")
obj2.owner("Rohan")