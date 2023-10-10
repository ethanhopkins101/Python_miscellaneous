#Description:
#1-Write a Python program that prints a triangular pattern like the ones shown below in the examples.
#2-Each row must have its corresponding number of asterisks. The first row contains one asterisk. The second row contains two asterisks. The third row contains three asterisks and so on.
#3-The number of rows should be determined by the value of n, a value entered by the user

def triangle_asterisks(row_number):
    for n in range(1,row_number+1):
        print('* '*n)


row_number=int(input("rows: "))
triangle_asterisks(row_number)