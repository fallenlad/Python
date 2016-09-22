#!/usr/bin/env python3
"""Program to print the even numbers between 1 and 100 using loop structures
a) using for loop, use continue/break/pass statement to skip odd numbers
    i) break the loop if the value is 50
    ii) use continue statement for the values 10, 20, 30, 40, 50
b) using while loop, use continue/break/pass statement to skip odd numbers
    i) break the loop if the value is 90
    ii) use continue for the values 60, 70, 80, 90

Usage:  python3 prg19.py
"""

def init():
    """Display the even numbers between 1 and 100 using loop statement"""
    #Using for loop to print even numbers
    for i in range(1,101):
        if i % 2 == 0:
            print(i)
            if i == 50:
                break
            elif i == 10:
                continue
            elif i == 20:
                continue
            elif i == 30:
                continue
            elif i == 40:
                continue
            elif i == 50:
                continue
        else:
            continue
    #Using while loop to print even numbers
    num = 1
    while num < 101:
        num = num + 1
        if num % 2 == 0:
            print(num)
            if num == 90:
                break
            elif num == 60:
                continue
            elif num == 70:
                continue
            elif num == 80:
                continue
            elif num == 90:
                continue
        else:
            continue

if __name__ == '__main__':
    init()
