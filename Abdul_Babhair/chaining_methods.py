# from flask import session
class Bike(object):
	"""docstring for bike"""
	def __init__(self, price, max_speed):
		self.miles = 0
		self.price = price
		self.max_speed = max_speed
	
	def displayinfo(self):
		print "the bike costs $"+str(self.price)+", and it's maximum speed is "+str(self.max_speed)+", and has "+str(self.miles)+" miles on it."
		# return self

	def ride(self):
		print "Riding"
		self.miles += 10
		return self
		# count = 10
		# print count
		# if 'count' not in session:
		# 	session["count"] = count
		# session['count']+=10
		# print session['count']

	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -=5
		return self
		

Bike1 = Bike(200, '25 mph');
Bike2 = Bike(300, '35 mph');
Bike3 = Bike(100, '10 mph');
# print Bike1.miles
# print Bike2.price

Bike1.ride().ride().ride().reverse().displayinfo()
Bike2.ride().ride().reverse().reverse().displayinfo()
Bike3.reverse().reverse().reverse().displayinfo()


# Bike1.ride();
# Bike1.ride();
# Bike1.ride();
# Bike1.reverse();
# Bike1.displayinfo();

# Bike2.ride();
# Bike2.ride();
# Bike2.reverse();
# Bike2.reverse();
# Bike2.displayinfo();

# Bike3.reverse();
# Bike3.reverse();
# Bike3.reverse();
# Bike3.displayinfo();