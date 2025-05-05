#!/usr/bin/python3
import sys

# Function: factorial
# Description: This function calculates the factorial of a given number n recursively.
# The factorial of a number is the product of all positive integers less than or equal to n.
# Example: factorial(4) returns 4 * 3 * 2 * 1 = 24.
#
# Parameters:
#   n (int): The number for which the factorial is to be calculated.
#            Must be a non-negative integer (n >= 0).
#
# Returns:
#   int: The factorial of the input number n.
#        Returns 1 if n == 0, as factorial(0) is defined as 1.

def factorial(n):
    if n == 0:
        return 1  # Base case: factorial(0) is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Read the input number from the command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
