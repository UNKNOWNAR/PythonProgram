class Vehicle:
    def general_use(self):
        print("genral use: transportation")
class Car(Vehicle):
    def __init__(self):
        print("I am a Car")
        self.wheel = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_use()
        print("sprcific usage: comute to work and vacation with family")

class Bike(Vehicle):
    def __init__(self):
        print("I am a Bike")
        self.wheel = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_use()
        print("sprcific usage:road trip,racing")
c = Car()
c.specific_usage()
b = Bike()
b.specific_usage()
print(isinstance(c,Car))
print(isinstance(c,Bike))