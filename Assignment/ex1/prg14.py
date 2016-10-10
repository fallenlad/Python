#!/usr/bin/env python3
"""Program to create two list A and B such that list A contains employee id and
list b contains employee name(10 entries in each list) and perform the below
operations
a) print all the names 
b) read the index as input and print the corresponding name and id
c) print the names from 4th position to 9th position
d) print all names from 3rd position till end of the list
e) repeat the list elements by N number of times where N will be an user input
f) concatenate two lists and print the output
g) print elements of list A and B side by side

Usage: python3 prg14.py
"""


def init():
    """Fetch two list and display the output of the operations on the list"""
    emp_id = []
    emp_name = []
    position = 0
    emp_id = get_employee_ids()
    emp_name = get_employee_names()
    print("Employee names:")
    for item in emp_name:
        print(item)
    position = int(input("Enter the record index to fetch:"))
    if position > -1 and position < len(emp_id):
        print("Id:", emp_id[position], " Name: ", emp_name[position])
    else:
        print("Record not available")
    print("List of names from 4th to 9th position")
    for name in emp_name[3:9]:
        print(name)
    print("List of names from 3rd position to end of list")
    for item in emp_name[2:]:
        print(item)
    #Repeat list items for N number of times
    print("Enter the number of times list needs to be repeated")
    repeat_list_count = int(input())
    counter = 0
    while counter < repeat_list_count:
        for item in range(10):
            print("Id:", emp_id[item], " Name: ", emp_name[item])
        counter += 1
    #Concatenate two lists
    print("Concatenating two list")
    emp_id_name = emp_id + emp_name
    for item in emp_id_name:
        print(item)
    #print the records side by side
    for item in range(10):
        print("Id:", emp_id[item], " Name: ", emp_name[item])

def get_employee_ids():
    emp_id = []
    emp_id.append(321)
    emp_id.append(653)
    emp_id.append(626)
    emp_id.append(8732)
    emp_id.append(12)
    emp_id.append(1664)
    emp_id.append(74)
    emp_id.append(135)
    emp_id.append(6423)
    emp_id.append(235)
    return emp_id

def get_employee_names():
    emp_name = []
    emp_name.append("Adam")
    emp_name.append("Ellen")
    emp_name.append("Yakshi")
    emp_name.append("Rahul")
    emp_name.append("Rohit")
    emp_name.append("Anna")
    emp_name.append("Dinesh")
    emp_name.append("Brad")
    emp_name.append("Cristine")
    emp_name.append("Diya")
    return emp_name

if __name__ == '__main__':
    init()
