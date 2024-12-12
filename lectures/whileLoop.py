## while loop = execute some code WHILE some condition remains true

food= input("Enter a food you like (q to quit)): ")
while food != "q":
   print(f"You like {food}")
   food = input("Enter another food you like (q to quit)): ")
print("Bye")


## Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be <=0")

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("rate can't be <=0")
    else:
        break

while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("time can't be <=0")

total = principle * pow((1+rate/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")

