# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(help(capitals))

# print(capitals.get("USA"))
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})

# to delete a pair can use pop method
# capitals.pop("China")

# keys = capitals.keys()
#
# for key in capitals.keys():
#     print(key)

# items = capitals.items()
# print(items)

# for key,value in capitals.items():
#     print(f"{key}: {value}")

## Concession stand program

# menu= {"pizza":3.00,
#        "nachos":4.50,
#        "fries":2.50,
#        "chips": 1.00,
#        "soda":3.00}
#
# cart = []
# total = 0
#
# print("--------MENU--------")
# for key,value in menu.items():
#     print(f"{key:10}: ${value}")
# print("--------------------")
#
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food== "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
#
# print("--------------------")
# print(f"Total is: ${total: .2f}")