#!/usr/bin/env python3
"""Program to receive 5 command line arguments and print each of them
separately

Usage: python3 prg5a.py arg1 arg2 etc
"""

import sys


def display_cmdline_arg(cmdArgument):
    """Fetch a list and display the first five items

    Args:
        cmdArgument - List of items to be displayed
    """
    argumentCount = 0
    for item in cmdArgument:
        print(item)
        argumentCount += 1
        if argumentCount == 5:
            break

if __name__ == '__main__':
    cmdArgument = sys.argv
    cmdArgument.pop(0)
    display_cmdline_arg(cmdArgument)
