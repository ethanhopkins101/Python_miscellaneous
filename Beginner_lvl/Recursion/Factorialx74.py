#Description:
#1-Write a Python program that calculates and prints the value of the factorial of the number num using recursion.
#2-The factorial of a number x is denoted by x! and it is equal to x * (x-1) * (x-2) * ... * 1, the product of all positive integers less than or equal to the number.
#3-The value of 0! is equal to 1 by mathematical convention.

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))