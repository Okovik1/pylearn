## Conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                            Print or assign one of two values based on a condition
#                            X If condition else Y

## logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True ||
#                     and = both conditions nust be True &&
#                     not = inverts the condition (not False, not True) !=

import math
temp = 20
is_raining = True
is_sunny = True

if temp >=28 and not is_sunny:
   print("It is how outside")
   print("It is cloudy")
elif temp <= 0 and is_sunny:
   print("It's cold outside")
elif 28>temp>0 and not is_sunny:
   print("Wow you are lucky")
else :
   print("the weather is not that great")

num = 5
# print (X if condition else Y)
# print("Positive" if num>0 else "Negative")

result = "EVEN" if num %2 ==0 else "ODD"


if temp>35 or temp < 0 or is_raining:
   print("The outdoor event is cancelled")
else :
   print("Welcome to the event!")


a = float(input("Enter the length of a circle:"))
b = float(input("Enter the width of a circle:"))

c= math.sqrt(pow(a,2)+pow(b,2))
print(f"Your c is {round(c,2)} cm")

c = 2*math.pi*radius

print(f"Your radius is {round(c,2)} cm")

area = math.pi*pow(radius,2)
print(f"Your radius is {round(area,2)} cm")

name = input ("Enter your full name:")

nameLength = len(name)
nameSpace = name.isalpha()
nameDigit = name.isdigit()

if nameLength<=12 and nameSpace and not nameDigit:
  print("You have a valid username")
else: print("check your input")


result = len(name)
result1 = (name.find(" "))
result2 = name.rfind(" ")
print(result2)
name = name.capitalize()
print(name)
