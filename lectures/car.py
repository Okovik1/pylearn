
class Car:

# for protected "_" for private "__" for variables and methods

    wheels= 4


    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


car1 = Car("BMW", 1995, "Black", False)
car2 = Car("Mercedes", 2000, "Blue", True)

