#variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# Global = outside of any functions

#Local scope variables a and b
def func1():
    a=1
    print(a)

def func2():
    b=2
    print(b)

x = 3

#built-in variables from packages, for example from math import e

