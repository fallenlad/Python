#!/usr/bin/env python3
"""Program to generate fibonacci series.
a) number of elements printed in the series should be N numbers where N is any
positive integer
b) generate the series until the element in the series is less than max number

Usage: python3 prg20.py
"""


def init():
    """Fetch the iteration count, max number and display the fibonacci number
    for both instance"""
    #Output for iterations input case
    iteration = int(input("Enter the number of iterations:"))
    series = []
    if iteration == 1:
        series.append(0)
    elif iteration == 2:
        series.append(0)
        series.append(1)
    elif iteration > 2:
        series.append(0)
        series.append(1)
        while len(series) < iteration:
            item_count = len(series)
            series.append(series[item_count - 1] + series[item_count - 2])
    else:
        print("Enter a positive number")
    if len(series) > 0:
        print(series)
    #Output for max number input case
    num = int(input("Enter the maximum number for series generation:"))
    series.clear()
    if num == 0:
        series.append(0)
    elif num == 1:
        series.append(0)
        series.append(1)
    elif num > 1:
        series.append(0)
        series.append(1)
        while num > 1:
            item_count = len(series)
            new_item = series[item_count - 1] + series[item_count - 2]
            if new_item <= num:
                series.append(new_item)
            else:
                break
    else:
        print("Enter a positive number")
    if len(series) > 0:
        print(series)

if __name__ == '__main__':
     init()
