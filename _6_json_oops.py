import json
import os

class Employee:
	def employee_details(self,num):
		file = open(os.getcwd() + "/Python/_0_Assignments/employee.json")
		data = json.load(file)
		if num:
			return f"Employee {num} : {data[f'Employee_{num}']}"

lst = []

obj1 = Employee()
data= obj1.employee_details(1)
lst.append(data)

obj2 = Employee()
data= obj2.employee_details(2)
lst.append(data)

obj3 = Employee()
data= obj3.employee_details(3)
lst.append(data)

obj4 = Employee()
data= obj4.employee_details(4)
lst.append(data)

obj5 = Employee()
data= obj5.employee_details(5)
lst.append(data)

print("Employee Details:")
for i in range(5):
	print(lst[i])