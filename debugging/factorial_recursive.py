#!/usr/bin/python3
import sys

# Function description: Calculates the factorial of a given number recursively.
def factorial(n):
    # Parameters:
    #   n (int): The number whose factorial is to be calculated.
    
    # Returns:
    #   int: The factorial of the input number n.
    
    # Base case: If n is 0, return 1, as the factorial of 0 is 1.
    if n == 0:
        return 1
    # Recursive case: If n is not 0, calculate the factorial recursively by multiplying n with the factorial of (n-1).
    else:
        return n * factorial(n-1)

# Usage: ./factorial_recursive.py <number>
# Example: ./factorial_recursive.py 4
if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
