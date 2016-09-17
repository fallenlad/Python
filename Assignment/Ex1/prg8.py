#!/usr/bin/env python3
"""Program to create a tuple with 10 items in it and perform the below
operations
a) Print all the elements
b) Perform slicing
c) Perform repetition with * operator
d) Concatenate with other tuple type

Usage: python3 prg8.py
"""


def init():
    """Perform operations on the tuple object and display the results"""
    x = (1, 231, 14, 61, 56, 85, 23, 87, 101, 712)
    print("Items in tuple:")
    print(x)
    print("Slicing elements from 5 to 8")
    print(x[4:8])
    print("Repetition with * operator")
    print(x * 2)
    y = (1, 2, 3)
    print("Concatenation with another tuple %s" % (y,))
    print(x + y)

if __name__ == '__main__':
    init()
