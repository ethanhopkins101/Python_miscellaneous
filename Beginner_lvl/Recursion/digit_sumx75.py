#Description:
#1-Write a Python program that calculates and prints the sum of the digits of a positive integer num.
#2-The program must find the sum recursively.
#3-If the integer has only one digit, print the integer as the total sum.

def digit_sum(n):
    if n%10==n:
        return n
    else:
        return n%10+digit_sum(n//10)
    
print(digit_sum(111))