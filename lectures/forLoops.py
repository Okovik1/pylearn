## For loops = execute a block of code a fixed number of times.
#              You can iterate over a range, string, sequence, etc.
import time

for x in range(1,11):
    print(x)

for x in reversed(range(1, 11)):
        print(x)

#with step
for x in range(1, 11,3):
        print(x)

# to skip a number over iteration you can use continue word
for x in range (1,21):
        if x ==13:
                continue
        else:
                print(x)

credit_number ="1234-5678-9101-4321"
#
for x in credit_number:
        print(x)

## nested loop = a loop with another loop (outer,inner)
#                outer loop:
#                  inner loop:
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    sec = x%60
    min = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{min:02}:{sec:02}")

    time.sleep(1)

print("TIME'S UP!")