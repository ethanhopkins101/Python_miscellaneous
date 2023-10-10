#Description:
#1-Write a Python program that prints a string reversed using a loop.
#2-All the characters must be on the same line in reverse order.

def reverse_string(string_a):
    result=''
    for i in range(1,len(string_a)+1):
        result+=string_a[-i]
    return result

string_a=input("String: ")
result=reverse_string(string_a)
print(result)