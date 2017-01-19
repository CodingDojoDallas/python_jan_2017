class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax=0.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = tax
		self.display_all()

	def display_all(self):
		print "Price: {}, Speed: {}, Fuel: {}, Mileage: {}, Tax: {}%".format(self.price, self.speed, self.fuel, self.mileage, int(self.tax * 100))

Car(2000, "35mph", "Full", "15mpg")
Car(2000, "5mph", "Not Full", "105mpg")
Car(2000, "15mph", "Kind of Full", "95mpg")
Car(2000, "25mph", "Full", "25mpg")
Car(2000, "45mph", "Empty", "25mpg")
Car(20000000, "35mph", "Empty", "15mpg")