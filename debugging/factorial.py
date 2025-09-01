#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Number must be zero or positive.")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except (IndexError, ValueError) as e:
        print(f"Error : {e}")
