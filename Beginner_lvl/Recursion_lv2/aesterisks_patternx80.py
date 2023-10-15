#Description:
#1-Write a Python program that prints the pattern of asterisks shown below for a given value of n.
#2-The program must include a recursive function.
#3-n represents the number of rows in the resulting pattern and the number of asterisks printed on the first row
'''
For n = 6:
******
*****
****
***
**
*
'''
def aesterisks(n):
    if n<1:
        return
    else:
        print('*'*n)
        aesterisks(n-1)

print(aesterisks(6))