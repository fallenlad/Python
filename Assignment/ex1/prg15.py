#!/usr/bin/env python3
"""Program to create a list and check if a name exists in the list
a) use membership operator to check the presence of the element
b) perform above task without using the membership operator
c) print the elements of the list in reverse direction

usage: python3 prg15.py
"""


def init():
    """Fetch the name and display the results of the above operation"""
    names = get_names()
    find_name = input("Enter the name to search for:")
    #using membership operator
    if find_name in names:
        print("Name exists in the list")
    else:
        print("Name not found")
    #using for loop to check if the element exists in the list
    has_element = False
    for item in names:
        if item == find_name:
            has_element = True
            break
    if has_element:
        print("Name exists in the list")
    else:
        print("Name not found")
    names.reverse()
    print(names)

def get_names():
    name = []
    name.append("Dinesh")
    name.append("Rhonda")
    name.append("Terry")
    name.append("Amy")
    name.append("Amrita")
    return name

if __name__ == '__main__':
    init()
