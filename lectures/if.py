# if = Do some code only if some condition is True
#      Else do something else

#Python calculator

operator = input("Enter operator (+ - * /):")
num1 = float(input("Enter first nuber:"))
num2=float(input("Enter second number:"))

if operator == "+":
   result = num1+num2
   print(f" result of the operation {num1} + {num2} = {round(result,3)}")
elif operator == "-":
   result = num1 - num2
   print(f" result of the operation {num1} - {num2} = {round(result,3)}")
elif operator == "*":
   result = num1 * num2
   print(f" result of the operation {num1} * {num2} = {round(result,3)}")
elif operator == "/":
   result = num1 / num2
   print(f" result of the operation {num1}/{num2} = {round(result,3)}")
else:
   print(f"{operator} is not a valid operator")

# This is my first Py program

print("I like pizza")
print("It's really good!")

