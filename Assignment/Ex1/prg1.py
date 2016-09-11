#!/usr/bin/env python3
"""
    Program to add, subtract, multiply and divide two numbers

Usage: python3 prg1.py
"""
def init():
    """ Fetch two numbers and display the results of addition, subtraction,
    multiplication and division operations"""
    a = int(input())
    b = int(input())
    print("Add: %d" % sum(a,b))
    print("Subtract: %d" % subtract(a,b))
    print("Multiply: %d" % multiply(a,b))
    print("Divide: %d" % divide(a,b))

def sum(a,b):
    """Add two numbers

    Args:
        Two numbers that are to be added

    Returns:
        Sum of two given numbers
    """
    return a+b

def subtract(a,b):
    """Subtract two numbers

    Args:
        Two numbers that are to subtracted

    Returns:
        Subtracted result of two given numbers
    """
    return a-b

def multiply(a,b):
    """Multiply two numbers

    Args:
        Two numbers that are to be multiplied

    Returns:
        Multiplied result of two given numbers
    """
    return a*b

def divide(a,b):
    """Divide two numbers

    Args:
        Two numbers that are to be divided

    Returns:
        Division result of two given numbers
    """
    return a/b

if __name__ == '__main__':
    init() #Initialize the program

