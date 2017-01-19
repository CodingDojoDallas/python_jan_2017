class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		print "Walking ..."

	def run(self):
		self.health -= 5
		print "Running ..."

	def displayhealth(self):
		print self.name+' has a health of '+str(self.health)

class Dog(Animal):	
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		print "petting"
		
class Dragon(Animal):
	"""docstring for Dragon"""
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		print "flying"

	def displayhealth(self):
		print "this is a Dragon!"
		super(Dragon, self).displayhealth()
		

dragon = Dragon('Bob')

for i in range(1,4):
	dragon.walk()

for i in range(1,3):
	dragon.run()
	dragon.fly()

dragon.displayhealth()
