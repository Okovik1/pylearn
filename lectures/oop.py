# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex . phone, cup, book
#          You need a class to create many objects
# class = (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("BMW", 1995, "Black", False)
car2 = Car("Mercedes", 2000, "Blue", True)

car1.describe()
car2.stop()
