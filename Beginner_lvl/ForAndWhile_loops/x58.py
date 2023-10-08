#Description:
#1-Write a Python program that prints the integers between a given number n and 1 (in descending order, both inclusive).
#2-The value of n should be entered by the user and you may assume that it is an integer greater than or equal to 1.
#3-Use a loop to print each number on a separate line.

input=int(input("Type in a number: "))
for number in range(input,0,-1):
    print(number)