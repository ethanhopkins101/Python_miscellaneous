#Description:
#1-Write a Python program that calculates and prints the sum of the first 100 non-negative integers (from 1 to 100).
#2-Use a loop to find this sum.

sum=0
for number in range(101):
    sum+=number
print(sum)