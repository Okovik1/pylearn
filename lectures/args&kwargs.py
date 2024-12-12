## *args = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments
#           *unpacking operator
#           1. positional 2. default 3.KEYWORD 4. ARBITRARY

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#
#     print(f"{kwargs.get('street')}")
#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zipcode')}")
#
# shipping_label("Bro",
#                "Smth",
#                "Code",
#                street = "123 Fake",
#                city= "Detroit",
#                state= "MI",
#                zipcode="54321")

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1,2,3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Bro","Smth","Code")

# def address(**kwargs):
#   for key, value in kwargs.items():
#       print(f"{key} : {value}")
#
# address(street = "123 Fake",
#         city= "Detroit",
#         state= "MI",
#         zipcode="54321"  )


