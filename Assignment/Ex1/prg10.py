#!/usr/bin/env python3
"""Perform addition, subtraction, multiplication, division, modulus, exponent
and floor division operations using assignment operators"""


def init():
    """Fetch two numbers and display the results of addition, subtraction,
    multiplication, division, modulus, exponent and floor division operation
    """
    a = int(input())
    b = int(input())
    print("Addition: %d" % addition(a,b))
    print("Subtraction: %d" % subtraction(a,b))
    print("Multiplication: %d" % multiplication(a,b))
    print("Division: %f" % division(a,b))
    print("Modulus: %d" % modulus(a,b))
    print("Exponent: %d" % exponent(a,b))
    print("Floor division: %d" % floor_division(a,b))

def addition(a,b):
    a += b
    return a

def subtraction(a,b):
    a -= b
    return a

def multiplication(a,b):
    a *= b
    return a

def division(a,b):
    a /= b
    return a

def modulus(a,b):
    a %= b
    return a

def exponent(a,b):
    a **= b
    return a

def floor_division(a,b):
    a //= b
    return a

if __name__ == '__main__':
    init()
