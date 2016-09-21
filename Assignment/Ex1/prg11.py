#!/usr/bin/env python3
"""Program to perform all bitwise operations on two numbers

Usage: python3 prg11.py
"""


def init():
    """Fetch two numbers and display the results of all bitwise operations"""
    print("Enter two numbers:")
    a = int(input())
    b = int(input())
    print("Binary AND: ", a & b)
    print("Binary OR: ", a | b)
    print("Binary XOR: ", a ^ b)
    print("Binary ones complement: %d %d" %(~a,~b))
    print("Binary left shift on first input by 2: ", a << 2)
    print("Binary right shift on first input by 2: ", a >> 2)

if __name__ == '__main__':
    init()
