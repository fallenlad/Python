#!usr/bin/env python3
"""Program to read a string and print each character separately.
    also do
        a) slice the string using [:]operator to create subtstrings
        b) repeat the string 100 times using the * operator
        c) read the second string and concatenate it with the first string using
        + operator

Usage: python3 prg6.py
"""


def init():
    """Fetch strings and display the results of the operations listed"""
    str = get_statement()
    print("Characters in string:\n")
    for char in str:
        print(char)
    print("Slicing text using [:] operator: (from start of the string till 3 characters)")
    print(str[0:3])
    print("\nRepeat the string 100 time using * operator")
    print(str * 100)
    print("\nConcatenation with second string:")
    b = get_statement()
    print(str + b)

def get_statement():
    """Fetch an input statement from user at runtime

    Returns:
        Statement inputted by user
    """
    statement = input("Please enter the string:\n")
    return statement

if __name__ == '__main__':
    init()
