class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print "Price: {}, Maximum Speed: {}, Total Miles: {}".format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print "Riding..."
		self.miles += 10
		return self

	def reverse(self):
		if self.miles == 0:
			print "Cannot reverse"
			return self
		print "Reversing..."
		self.miles -= 5
		return self

bike1 = Bike(200, "25mph")
bike2 = Bike(150, "20mph", 100)
bike3 = Bike(300, "35mph", 30)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()