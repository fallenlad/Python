#!/usr/bin/env python3
"""Program to find the biggest of 3 numbers (use if statement)

Usaage: python3 prg2.py
"""

def init():
    """Fetch three numbers and display biggest of the three"""
    a = int(input())
    b = int(input())
    c = int(input())
    print("Biggest number is %d" % find_biggest_number(a,b,c))

def find_biggest_number(a,b,c):
    """Find the biggest of the given three numbers

    Args:
        Three numbers

    Returns:
        Biggest of the three numbers inputted
    """
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

if __name__ == '__main__':
    init()

