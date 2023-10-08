#Description:
#1-Write a Python program that prints the multiplication table for a positive integer n.
#2-The values displayed should go from n x 1 up to n x 10 with a descriptive format (as shown below).
#3-Use a loop to implement your solution.

'''==== Multiplication Table of 3 ====
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30'''

input=int(input("Type in a number: "))

for multiplier in range(1,11):
    print(f'{input} x {multiplier} = {input*multiplier}'.format(input=input,multiplier=multiplier))