#!/usr/bin/env python3
"""Program to find the biggest and smallest of N numbers (use functions to find
the biggest and smallest numbers)

Usage: python3 prg17.py
"""

def init():
    """Fetch 5 numbers and display the smallest and biggest number"""
    num = []
    print("Enter 5 numbers:")
    for item in range(5):
        num.append(int(input()))
    print("Biggest number: %d"% get_biggest_number(num))
    print("Smallest number: ", get_smallest_number(num))

def get_biggest_number(num):
    """Find the biggest number in the list

    Args:
        list of numbers

    Returns:
        biggest number in the list
    """
    big = 0
    for item in num:
        if item > big:
            big = item
    return big

def get_smallest_number(num):
    """Find the smallest number in the list

    Args:
        list of numbers

    Returns:
        smallest number in the list
    """
    small = num[0]
    for item in num:
        if small > item:
            small = item
    return small

if __name__ == '__main__':
    init()
