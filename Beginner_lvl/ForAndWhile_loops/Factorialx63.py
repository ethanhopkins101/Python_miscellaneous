#Description:
#1-Write a Python program that calculates the factorial of a given number n.
#2-The value of n should be entered by the user.
#3-The program must print the result and use a loop to calculate it.
#4-The factorial of a number n is denoted as n! and it is the result of multiplying all the positive integers that are less than or equal to n.

input=int(input('type in a number: '))
result=1
string_a=''
for number in range(input,0,-1):
    string_a=string_a+f'{number} x '
    result=result*number
print(input,'!=',string_a.strip('x '),'=',result)