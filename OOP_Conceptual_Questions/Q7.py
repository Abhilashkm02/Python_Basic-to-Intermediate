'''Inheritance:
    create a base class called vehicle with a start method that prints "Vehicle started".
    create a subclass called bike with an additional method called ride that prints "Bike is being ridden".
    create an object of the bike class and call both the start and ride methods.'''

class vehicle:
    def start(self):
        print("vehicle has started")

class bike(vehicle):
    def ride(self,name):
        print(f"{name} is being ridden")

# Create an object of the bike class
my_bike = bike()
# Call the start method from the base class
my_bike.start()
# Call the ride method from the subclass
my_bike.ride("Java")