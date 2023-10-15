#Description:
#1-Write a Python program that find the value of a raised to the power b recursively.
#2-The operation is a**b in Python, where a is the base and b is the exponent.
#3-If the value of b is 0, the result is automatically 1 because every number raised to the power 0 is 1.

def raised_pow(n,p):
    if p==0:
        return 1
    else:
        return n*raised_pow(n,p-1)
print(raised_pow(5,3))