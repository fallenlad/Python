#!/usr/bin/env python3
"""Program to find the given number is a prime number or not

Usage: python3 prg4.py
"""

from math import sqrt
from math import ceil

def init():
    """Fetch the number and display if it is a prime number or not"""
    num = int(input())
    if is_prime_number(num):
        print("%d is a prime number" % num)
    else:
        print("%d is not a prime number" % num)

def is_prime_number(num):
    """Check if the given number is prime number or not

    Args:
        Number to be validated

    Returns:
        True if the number is a prime number, false if it's not
    """
    nearestSquareRoot = get_nearest_square_root(num)
    primeNumbers = get_prime_numbers(nearestSquareRoot)
    for primeNumber in primeNumbers:
        if (num % primeNumber) == 0:
            return False
    return True

def get_nearest_square_root(num):
    """Fetch the greatest and nearest square root of the given number

    Args:
        Number to be calculated against

    Returns:
        Nearest square root for the given number
    """
    squareRoot = ceil(sqrt(num))
    while num >= (squareRoot * squareRoot):
        squareRoot += 1
    return squareRoot

def get_prime_numbers(num):
    """Fetch the list of prime numbers that are less than the given number

    Args:
        Number to be calculated against

    Returns:
        List of prime numbers
    """
    primeNumbers = []
    if num > 2:
        primeNumbers += get_prime_numbers(num - 1)
        for primeNumber in primeNumbers:
            if (num % primeNumber) == 0:
                return primeNumbers
        primeNumbers.append(num)
        return primeNumbers
    elif num == 2:
        return [2]

if __name__ == '__main__':
    init()
