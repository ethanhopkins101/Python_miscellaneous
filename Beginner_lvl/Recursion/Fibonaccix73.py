#Description:
#1-Write a Python program that calculates and prints the nth Fibonacci number.
#2-The value of n represents the position of the element in the sequence.
#3-The initial value of n should be 0.
#You may assume that the value of n is a non-negative integer.

def fibonnaci(n):
    if n<2:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
print(fibonnaci(3))