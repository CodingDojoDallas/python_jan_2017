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

for x in range(0,3):
	bike1.ride()
bike1.reverse()
bike1.displayInfo()

for x in range(0,2):
	bike2.ride()
for x in range(0,2):
	bike2.reverse()
bike2.displayInfo()

for x in range(0,3):
	bike3.reverse()
bike3.displayInfo()