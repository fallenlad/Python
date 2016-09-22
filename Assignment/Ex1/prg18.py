#!/usr/bin/env python3
"""Program to print numbers from 1 to 100 using loop statements. Also using the
same loop print numbers from 100 to 1.
a) by using for loop
b) by using while loop
c) let mystring = "hellp world", print each character in mystring to separete
line using appropriate loop statements

Usage: python3 prg18.py
"""

def init():
    """Display numbers from 1 to 100 and also in reverese order using loop
    statements"""
    #print 1 to 100 using for loop
    for i in range(1,101):
        print(i)
    #print 100 to 1 using for loop
    for i in reversed(range(1,101)):
        print(i)
    #print 1 to 100 using while loop
    count = 1
    while count < 101:
        print(count)
        count += 1
    #print 100 to 1 using while loop
    count = 100
    while count > 0:
        print(count)
        count -= 1
    #print characters in the given string 
    mystring = "Hello World"
    for char in mystring:
        print(char)

if __name__ == '__main__':
    init()

