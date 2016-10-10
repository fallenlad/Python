#!/usr/bin/env python3
"""Program to find the biggest of 4 numbers
    a) read 4 numbers using input statment
    b) Extend the program to find the biggest of 5 numbers
    (use if, if else, elif and nested if statements)
"""


def init():
    """Fetch inputs and display the biggest of the numbers"""
    num = []
    for item in range(4):
        num.append(int(input()))
    print("Biggest number is %d" % get_biggest_number(num))
    num.append(int(input("Please enter one more number: ")))
    print("New Biggest number is %d" % get_biggest_number(num))

def get_biggest_number(num):
    big = 0
    if len(num) == 4:
        if num[0] > big:
            big = num[0]
        if num[1] > big:
            big = num[1]
        if num[2] > big:
            big = num[2]
        if num[3] > big:
            big = num[3]
        return big
    elif len(num) == 5:
        for item in range(5):
            if num[item] > big:
                big = num[item]
        return big
    else:
        return 0

if __name__ == '__main__':
    init()
