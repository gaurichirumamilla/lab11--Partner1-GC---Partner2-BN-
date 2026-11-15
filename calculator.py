"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
        if a < 0:
            raise ValueError
        else:
            try:
                return math.sqrt(a)
            except Exception as e:
                raise e
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e

def add(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    else:
        return a + b


def subtract(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    else:
        return a - b

def multiply(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    else:
        return a * b

def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    elif a == 0:
        raise ZeroDivisionError
    else:
        return b / a


def logarithm(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    else:
        return math.log(a,b)

def exponent(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    else:
        return a ** b
try:
    answer= divide(0,2)
    print(answer)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("value error")



