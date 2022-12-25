class User:
	def __init__(self,name,phone_num,email,address,password):
		self.name = name
		self.phone_num = phone_num
		self.email = email
		self.address = address
		self.password = password

	def __str__(self):
		return f"Name: {self.name} \nPhone number: {self.phone_num} \nEmail: {self.email} \nAddress: {self.address}"

	def order_history(self):
		pass

	def update_profile(self):
		pass

	def set_name(self,name):
		self.name = name

	def get_name(self):
		return self.name

	def set_phone_num(self,phone_num):
		self.phone_num = phone_num

	def get_phone_num(self):
		return self.phone_num

	def set_email(self,email):
		self.email = email

	def get_email(self):
		return self.email

	def set_address(self,address):
		self.address = address

	def get_address(self):
		return self.address

	def set_password(self,password):
		self.password = password

	def get_password(self):
		return self.password