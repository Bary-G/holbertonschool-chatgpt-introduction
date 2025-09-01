#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Recursively calculates the factorial of an integer n.

    Args:
        n (int): An integer whose factorial we want to calculate.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)