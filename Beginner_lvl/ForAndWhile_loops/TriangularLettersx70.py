#Description:
#1-Write a Python program that prints a triangular pattern made with letters (as shown below).
#2-The first row should have one letter A (in uppercase). The second row should have two letters B. The third row should have three letters C and so on.
#3-The number of rows is determined by the value of n, which is entered by the user.
#4-The letters must be separated by a space.

import string
def triangular_letters(rows):
    for i in range(1,rows+1):
        print('{letters} '.format(letters=string.ascii_uppercase[i-1])*i)

row_number=int(input('Row: '))
triangular_letters(row_number)