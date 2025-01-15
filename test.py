import math

#  a = 3.6
#  b=round(a)
#  print(b)
#
# name = input("Enter your name: ")
# year = int(input("Enter your year of birth: "))
# age = 2024-year
# print(f'You are {name}')
# print(f'You are {age} years old')

# a=0
#
# while a<10:
#     a+=1
#     if a%3==0:
#         print(a)
#         break
# else:
#     print("While loop has been finished")

# k= [1,2,2,3,4,3,100]
# k[0] = 3
# k.append(8)
# k.remove(100)
# # print(k)
#
# fruits = ['apple','banana','orange']
# fruits.remove('apple')
# fruits.pop()
# fruits.insert(0,'apple2')
# m = fruits.index('apple2')
# print(m)

# list a = fruits
# list b = empty list , should contain elements of list A
#
# a = ["apple","banana","orange"]
# k = a.copy()
# # i = []
# # for x in a:
# #     i.append(x)
#
# # k=a
# a.append("coconut")


# i = [x for x in a ]
# print(k)

# def key_function(person):
#     return person["age"]
#
# people = [{"name": "Tom",
#            "age": 34},
#           {"name": "Kate",
#            "age": 24},
#           {"name": "Nick",
#            "age": 25}]
#
# people.sort(key=key_function)
#
# # sorted(people,key = lambda x: x["age"])
# print(people)

def my_function(*args, **kwargs):
    """
    description
    parameters
    *args :
    **kwargs :
    """
    print(args)
    print(kwargs)

print(my_function.__doc__)

my_function(1,2,3,4,5,6,["a","b","c"], name="Kate", age = 13)

k= [1,2,2,3,4,3,100]

# a = [x for x in range(1,101) if x%2==0]
a=list(range(1,100))

# ! lambda functions map and reduce

even_nums= list(filter(lambda x: x%2==0, a )) # list contains even number

"""
b (int) : description of variable
"""
b : int = 2

print(even_nums)

# b= {1,2,2,3,4,3}
# b.add(10)
#
# c=(1,2,3,3,4,2)
# # c[0]=7
# print(c[0])
# print(b)


# while True:
#     try:
#         a = float(input("Enter first number : "))
#         symbol = input("Enter the operation (q-for exit) : ")
#         b = float(input("Enter second number: "))
#         if symbol== '+':
#             result = a+b
#             print(f'result is: {result}')
#         elif symbol== '-':
#             result = a-b
#             print(f'result is: {result}')
#         elif symbol == '*':
#             result = a * b
#             print(f'result is: {result}')
#         elif symbol == '/' :
#             result = a / b
#             print(f'result is: {result}')
#         else:
#             print("You exit the calculator")
#             break
#     except ZeroDivisionError:
#         print("You can not divide by zero!")
#     except Exception as e :
#         print(f"You should add an actual number! {e}" )
#     finally:
#         print("")








