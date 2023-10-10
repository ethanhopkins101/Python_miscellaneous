#Description:
#1-Write a Python program that prints Floyd's Triangle with n number of rows.
#2-The value of n should be entered by the user. You may assume that it is a positive integer.
#3-Floyd's Triangle is made with consecutive numbers that fill the rows of the triangle (as shown below)
'''If n is equal to 5:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15'''
def floyd_triangle(rows):
    k=1
    for i in range(1,rows+1):
        for j in range(i):
            print(k,end=' ')
            k+=1
        print()
        
'-------------------------------------'
row_number=int(input("Rows: "))
floyd_triangle(row_number)
