class car(object):
    def __init__(self, price, speed, fuel, mileage):

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price:", str(self.price)
        print "Speed:", str(self.speed)
        print "Fuel:", str(self.fuel)
        print "Mileage:", str(self.mileage)
        print "Tax:", str(self.tax)

car1 = car(2000, "35mph", "Full", "15mpg")
car2 = car(2000, "5mph", "Not Full", "105mpg")
car3 = car(2000, "15mph", "Kind of Full", "95mpg")
car4 = car(2000, "25mph", "Full", "25mpg")
car5 = car(2000, "45mph", "Empty", "25mpg")
car6 = car(20000000, "35mph", "Empty", "15mpg")

car1.display_all()
print "*"*50
car2.display_all()
print "*"*50
car3.display_all()
print "*"*50
car4.display_all()
print "*"*50
car5.display_all()
print "*"*50
car6.display_all()