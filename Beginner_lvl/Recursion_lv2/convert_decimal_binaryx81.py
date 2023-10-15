#Description:
#1-Write a Python program that converts a decimal number to binary using recursion.
#2-The function must return the binary representation as a string.
#3-The program must print the value returned.

def decimal_tobinary(n):
    if n==0:
        return '0'
    else:
        return decimal_tobinary(n//2)+str(n%2)
print(decimal_tobinary(2))