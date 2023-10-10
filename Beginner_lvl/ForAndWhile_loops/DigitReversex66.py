#Description:
#1-Write a Python program that prints the digits of a number in reverse order on the same line.
#2-If the number only has one digit, print this digit

def reverse_digit(number):
    result=''
    updated_number=number
    length=len(str(number))
    for i in range(length):
        result+=str(updated_number%10)
        updated_number//=10
    return result
number_a=int(input('number: '))
result=int(reverse_digit(number_a))
print(result)
print(type(result))