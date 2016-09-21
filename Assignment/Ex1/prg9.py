#!/usr/bin/env python3
"""Program to add, subtract, multiply and divide two complex numbers

Usage: python3 prg9.py
"""


def init():
    """Fetch two complex numbers and display the results of the operation"""
    print("Enter the first number")
    x = complex(input("Real part: ") + input("Imaginary part(include +/-): ")+"j")
    print("Enter the second number")
    y = complex(input("Real part: ") + input("Imaginary part(include +/-): ")+"j")
    print(x)
    print(y)
    print("Addition:", x+y)
    print("Subtraction:", x-y)
    print("Multiplication:", x*y)
    print("Division:", x/y)

if __name__ == '__main__':
    init()
