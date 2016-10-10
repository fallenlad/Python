#!/usr/bin/env python3
"""Program to receive 3 numbers as command line arguments and find the biggest
of the three

Usage: python3 prg5b.py arg1 arg2 etc
"""

import sys


def find_biggest_number(numbers):
    """Find the biggest number and display it

    Args:
        numbers - list of numbers
    """
    big = 0
    for item in numbers:
        if big < item:
            big = item
    print("Biggest number: %d" % big)


if __name__ == '__main__':
    cmdArgument = sys.argv
    #Remove the first item which contains the file name
    cmdArgument.pop(0)
    #Convert the list items to integer format
    numbers = [int(item) for item in cmdArgument]
    find_biggest_number(numbers)
