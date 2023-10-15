#Description:
#1-Write a Python program that prints a diamond made with asterisks where the diamond's height (number of rows) is determined by the value of the variable height
#2-You can (optionally) ask the user to enter the value of height.
#3-This value can only have an odd number of rows, so you should print a descriptive message if the user enters an even value.

def diamond_asterisks(rows):
    i=1
    inden=rows-1
    k=1
    while k>0:
        if i < rows//2:
            print(' '*inden+'*'*i)
            i+=1
            inden-=1
            k=i
        else:
            print(' '*inden+'*'*k)
            k-=1
            inden+=1

row_number=0
while True:
    row_number=int(input("Odd-Rows: "))
    if not(row_number%2==0) :
        break
diamond_asterisks(row_number)