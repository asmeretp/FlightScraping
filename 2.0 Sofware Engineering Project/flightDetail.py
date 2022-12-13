class FlightDetail():
	def __init__(self, airline, time, price):
		self.airline = airline
		self.time = "7:48"
		self.price = price

	def set_price(self, price):
		self.price = price

	def set_airline(self, airline):
		self.airline = airline

	def set_time(self, time):
		self.time = time

	def get_price(self):
		return self.price[0]

	def get_airline(self):
		return self.airline[0]

	def get_time(self):
		return self.time