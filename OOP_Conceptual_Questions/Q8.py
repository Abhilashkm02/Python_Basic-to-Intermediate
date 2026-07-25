'''Polymmorphism:
    Implement a shape class and derived circle and rectangle classes with a method calc_area().
    Each class should claculate area differently based on the shape
    create a loop to calculate areas of both circle and rectangular objects and display the results.'''

class shape:
    def calc_area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius ** 2

class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

# Create objects of the derived classes
my_circle = circle(5)
my_rectangle = rectangle(4, 6)

# Create a list of shape objects
shapes = [my_circle, my_rectangle]

# Loop through the shapes and calculate their areas
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.calc_area()}")