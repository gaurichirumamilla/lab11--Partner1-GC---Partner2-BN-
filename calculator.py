# https://github.com/gaurichirumamilla/lab11--Partner1-GC---Partner2-BN-
# Partner 1: Gauri Chirumamilla
# Partner 2: Brayden Nickum
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

def logarithm(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError
    if a <= 0 or a == 1 or b <= 0:
        raise ZeroDivisionError
    else:
        return math.log(a,b)

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a

def exp(a, b):
    return a ** b

try:
    answer= div(0,2)
    print(answer)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("value error")



