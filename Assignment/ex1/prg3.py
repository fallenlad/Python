#!/usr/bin/env python3
"""Program to find the given number is odd or even

Usage: python3 prg3.py
"""


def init():
    """Fetch a number and display if it is odd or even number"""
    a = int(input())
    isEvenNumber = is_even_number(a)
    if isEvenNumber:
        print("%d is an even number" % a)
    else:
        print("%d is odd number" % a)

def is_even_number(a):
    """Check if the given number is even number

    Args:
        Number to be validated

    Returns:
        True if the number is an even number, false if it is an odd number
    """
    if (a%2) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    init()
