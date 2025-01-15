# a = "Test"
# print(a)
# b=None
# d= 3
# def holdsVariable():
#     global b
#     b=10
#     global d
#     d+=1
#     print(d)
# holdsVariable()
# if True:
#     c=8
# print(b)

# def addition(a,b):
#     return a+b
# def do_math(math_function):
#     return math_function
#
# add = do_math(addition)
# print(add(3,5))
# print(addition(3,3))

# def simple_decorator(func):
#     def wrapper():
#         print("Before calling func")
#         func()
#         print("After calling func")
#
#     return wrapper
#
#
# @simple_decorator
# def say_hello():
#     print("Hello!")
#
#
# # print(simple_decorator(say_hello))
# say_hello()
#
# import time
#
#
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time}')

    return wrapper


@timer
def count():
    lst = []
    for x in range(1, 1000001):
        lst.append(x)


count()

# Create a function which creates list which is using list comprehension ->
# create another function that create list of even numbers out of the created list (for loop)
# -> filter function


# Input: nums = [2, 7, 11, 15], target = 9
# берем первое значение из списка и складываем со всеми по порядку
# если сумма первого и х = 9 записываем во второй список
# Output: [0, 1]




# lst = [3, 2, 4]
# lst2 = []
# target = 6
# for x in lst:
#     for y in lst:
#         y += 1
#         if x + y == target:
#             lst2.append(lst.index(x))
#             lst2.append(lst.index(y))
#         else:
#             y += 1
#         x += 1
#
# print(lst2)


# def twoSum( nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
#
#     return []


def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        x = list(str(x))
        
        y =[]
        for char in reversed(x):
            print(char)
            y.append(char)
        return y==x

        # x = str(x)
        # y = []
        # for char in reversed(x):
        #     y = y.append(char)
        # if x ==y:
        #     return True
        #
        # return

print(isPalindrome(123))





