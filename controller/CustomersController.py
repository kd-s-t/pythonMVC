class CustomersController():

	def __init__(self, cm):
		self.__CustomersModel = cm

	def create(self):
		print('Enter your name:')
		name = input()
		print('Enter your address:')
		address = input()

		# here we access Model Customers
		cm = self.__CustomersModel.CustomersModel()
		response = cm.create(name, address)

		print(response)

	def read(self):
		# here we access Model Customers
		cm = self.__CustomersModel.CustomersModel()
		response = cm.read()

		for x in response:
		  print(x)

	def update(self):
		print('Search by id:')
		id = input()

		print('Edit name:')
		name = input()

		if name is "":
			print("Leaving name empty will update the value to empty as well.")

		print('Edit address:')
		address = input()

		if address is "":
			print("Leaving address empty will update the value to empty as well.")

		# here we access Model Customers
		cm = self.__CustomersModel.CustomersModel()
		response = cm.update(name, address, id)

		print(response)

	def delete(self):
		print('Search by id to delete:')
		id = input()

		# here we access Model Customers
		cm = self.__CustomersModel.CustomersModel()
		response = cm.delete(id)

		print(response)
