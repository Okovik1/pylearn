from typing import List

class Animal :


    color : str
    age : int
    legs : int

    def __init__(self,color:str, age : int, legs: int, name:str):
        self.color=color
        self.age=age
        self.legs=legs
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Cat (Animal):
    """
    Cat is a child of an Animal class
    """

    sound = "Meow"
    fruits : List[str] = []


    def __init__(self,color:str, age:int, legs:int,sound:str, name:str):
        # self.color = color
        # self.age = age
        # self.legs = legs
        super().__init__(color, age, legs, name)
        self.sound = sound


    def __len__(self):
        return 10

    def __mul__(self, other):
        return other

    def addFavoriteFruits(self,fruit:str):
        self.fruits.append(fruit)

    def displayFruits(self)->List[str]:
        return self.fruits


cat1 = Cat("Black", 1, 4, "Meow")
cat2 = Cat("White",12,4,"Meow")

cat1.addFavoriteFruits("apple")
cat1.addFavoriteFruits("orange")
print(cat1.displayFruits())

# print(cat1*15)
# print(len(cat1))
# print(cat1)
# print()

# print(cat1.color)
# print(cat1.age)
# print(cat1.legs)
# print(cat1.sound)

