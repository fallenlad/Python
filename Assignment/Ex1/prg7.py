#!/usr/bin/env python3
"""Program to create a list with 10 items in it and perform the below
operations
a) Print all the elements
b) Perform slicing
c) Perform repetition with * operator
d) Concatenate with other list

Usage: python3 prg7.py
"""


def init():
    """Perform operations on the list object and display the results"""
    x = [1, 231, 14, 61, 56, 85, 23, 87]
    x.append(100)
    x.append(91)
    print("Items in the list:")
    print(x)
    print("Slicing elements from 5 to 8")
    print(x[4:8])
    print("Repetition with * operator")
    print(x * 2)
    y = [1, 2, 3]
    print("Concatenation with another list %s" % y)
    print(x + y)

if __name__ == '__main__':
    init()
