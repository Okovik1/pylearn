# multiple inheritance = inherit from more that one parent class C(A,B)
# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A



class Animal:
    def eat(self):
        print("This animal is eating")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
rabbit.eat()
hawk.hunt()
fish.flee()
fish.hunt()