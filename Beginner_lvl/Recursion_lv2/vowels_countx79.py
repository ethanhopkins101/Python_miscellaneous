#Description:
#1-Write a Python program that counts the number of vowels in a string recursively.
#2-If the string is empty or only contains one consonant, print 0.
#3-The program should be case-insensitive. Therefore, vowels in uppercase should also be counted.

class Vowels():
    volwes='aeiuoyAEIUOY'


def vowels_count(s):
    if not s:
        return 0
    else:
        return int(s[-1] in Vowels.volwes)+vowels_count(s[:-1])

string_a='Amazing'
print(vowels_count(string_a))
