class bike(object):
    def __init__(self, price=None, max_speed=None):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
# function to display info about the bike
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
# function to ride and add miles to the bike
    def ride(self):
        print "Riding"
        self.miles+=10
        return self
# function to reverse and take away miles from the bike
    def reverse(self):
        print "Reversing"
        self.miles-=5
        return self

bike1 = bike(125, "15mph")
bike2 = bike(175, "20mph")
bike3 = bike(250, "30mph")


bike1.ride().displayInfo()

bike2.ride().displayInfo()

bike3.reverse().displayInfo()