class Animal(object):
    def __init__(self, name="animal"):
        self.name = name
        self.health = 100
    def walk(self):
        self.health-=1
    def run(self):
        self.health-=5
    def displayHealth(self):
        print self.name
        print self.health

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150
    def pet(self):
        self.health+=5

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__()
        self.health = 170
    def fly(self):
        self.health-=10
    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "this is a dragon!"

animal = Animal("cow")
for i in range (0,3):
    animal.walk()
for i in range (0,2):
    animal.run()
animal.displayHealth()

puppy = Dog()
for i in range (0,3):
    puppy.walk()
for i in range (0,2):
    puppy.run()
puppy.pet()
puppy.displayHealth()

dragon = Dragon()
for i in range (0,3):
    dragon.walk()
for i in range (0,2):
    dragon.run()
for i in range (0,2):
    dragon.fly()
dragon.displayHealth()