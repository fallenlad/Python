#!/usr/bin/env python3
"""Program to find if the given number is prime or not. Also generate all the
prime numbers between 1 and user inputted number

Usage: python3 prg16.py
"""

from math import sqrt

def init():
    """Fetch a number and display if it is a prime number or not. Also print
    all the prime numbers between 1 and input number"""
    num = int(input("Enter the number to check:"))
    square_root = get_nearest_square_root(num)
    prime_numbers = get_prime_numbers(square_root)
    prime = []
    for n in range(2, num + 1):
        is_prime = True
        for i in prime_numbers:
            if (n > i) and (n % i == 0):
                is_prime = False
                break
        if is_prime:
            prime.append(n)
    if num in prime:
        print("%d is a prime number" % num)
    else:
        print("%d is not a prime number" % num)
    print("List of prime numbers between 1 and %d" % num)
    print(prime)

def get_prime_numbers(square_root):
    """Find all the prime numbers less than the given number

    Args:
        maximum number until which prime numbers are to identified

    Returns:
       list of prime numbers less than the given number
    """
    prime_numbers = []
    for i in range(2 , square_root + 1):
        prime = True
        for pn in prime_numbers:
            if (i > pn) and (i % pn == 0):
                prime = False
                break
        if prime or i == 2:
            prime_numbers.append(i)
    return prime_numbers

def get_nearest_square_root(num):
    """Find the nearest square root greater than the given number

    Args:
        number to calculate the nearest square root

    Returns:
        nearest square root to the given number
    """
    square_root = round(sqrt(num))
    if num > (square_root * square_root):
        square_root += 1
    return square_root

if __name__ == '__main__':
    init()

