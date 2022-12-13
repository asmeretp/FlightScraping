class Flight():
	def __init__(self, departure , arrival, sdate, edate):
		self.departure = departure
		self.arrival = arrival
		self.sdate = sdate
		self.edate = edate

	def get_departure(self):
		return self.departure

	def get_arrival(self):
		return self.arrival

	def get_sdate(self):
		return self.sdate

	def get_edate(self):
		return self.edate
