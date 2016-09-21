#!/usr/bin/env python3
"""Program to read 10 numbers from user and find the average 
Also perform the below operations
a) Use comparison operator to check how many numbers are less than average and
print them
b) Check how many numbers are more than average
c) Check how many are equal to average
"""


import decimal

def init():
    """Fetch 10 numbers from user and display the results of the operations"""
    num = []
    print("Enter 10 numbers:")
    for item in range(10):
        num.append(int(input()))
    avg = round(decimal.Decimal(get_average(num)),0)
    print("Average of the numbers: %.2f" % avg)
    print("Numbers less than average: %d" % get_less_than_average(num, avg))
    print("Numbers greater than average: %d" % get_greater_than_average(num,
        avg))
    print("Numbers equal to average: %d" % get_equal_to_average(num, avg))

def get_average(num):
    """Find the average of numbers in the list

    Args:
        List of numbers

    Returns:
        Average of the given set of numbers
    """
    avg = 0
    for item in num:
        avg += item
    return avg/len(num)

def get_less_than_average(num, avg):
    """Find the count of inputted numbers that are less than the average

    Args:
        num - list of input values
        avg - average of the input values

    Returns:
        Count of numbers that are less than the average value
    """
    count = 0
    for i in num:
        if i < avg:
            count += 1
    return count

def get_greater_than_average(num, avg):
    """Find the count of inputted numbers that are greater than the average

    Args:
        num - list of input values
        avg - average of the input values
    Returns:
        Count of numbers that are greater than the average value
    """
    count = 0
    for i in num:
        if i > avg:
            count += 1
    return count

def get_equal_to_average(num, avg):
    """Find the count of inputted numbers that are equal to the average

    Args:
        num - list of input values
        avg - average of the input values
    Returns:
        Count of numbers that are greater than the average value
    """
    count = 0
    for i in num:
        if i == avg:
            count += 1
    return count

if __name__ == '__main__':
    init()
