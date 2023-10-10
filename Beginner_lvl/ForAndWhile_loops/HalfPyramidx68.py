#Description:
#1-Write a Python program that prints a pyramid pattern made with asterisks.
#2-The number of rows should be determined by the value of the variable n. This value will be entered by the user.
#3-You may assume that the value of n is a positive integer.

def half_pyramid(rows):
    inden=rows-1
    for n in range(1,rows+1):
        print(' '*inden+'*'*n)
        inden-=1
'--------------------------------'
row_number=int(input("Rows: "))
half_pyramid(row_number)