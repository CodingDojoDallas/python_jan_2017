class car(object):
	"""docstring for car"""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12;
		self.display_all()

	def display_all(self):
		print "Price: "+str(self.price)
		print "Speed: "+str(self.speed)
		print "Fuel: "+str(self.fuel)
		print "Mileage: "+str(self.mileage)
		print "Tax: "+str(self.tax)
		print "*"*50

car1 = car(5000, 140, 'gasoline', 7)
car2 = car(51000, 200, 'gasoline', 40)
car3 = car(15000, 160, 'gasoline', 19)
car4 = car(25000, 180, 'gasoline', 23)
car5 = car(52000, 220, 'gasoline', 35)
car6 = car(35000, 180, 'gasoline', 30)
