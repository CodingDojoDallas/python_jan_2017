class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        if self.miles >0:
            print self.miles
        else:
            self.miles = 0
            print self.miles
    def ride(self):
        print "riding"
        self.miles = self.miles +10
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        
bike1 = Bike(200, '25mph')
bike2 = Bike(500, '50mph')
bike3 = Bike(1000, '120mph')

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
print '____________________'
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
print '____________________'
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
#bike1.ride().ride().ride().reverse().displayInfo()
#bike2.ride().ride().reverse().reverse().displayInfo()
#bike3.reverse().reverse().reverse().displayInfo()
