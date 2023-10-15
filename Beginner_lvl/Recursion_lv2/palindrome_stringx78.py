#Description:
#1-Write a Python program that checks if a string is a palindrome or not (if it's read the same backwards and forwards).
#2-The program should be case-insensitive. Therefore, "A" should be considered equivalent to "a".
#3-Print True if the string is a palindrome. Else, print False.
#4-If the string is empty, print True.


s='12321'
c1=s[:len(s)//2]
c2=s[len(s)//2:]

if len(s)%2==0:
    c1=s[:len(s)//2]
    c2=s[len(s)//2:]
    print(c1==c2[::-1])
else:
    c1=s[:len(s)//2]
    c2=s[len(s)//2+1:] 
    print(c1==c2[::-1])