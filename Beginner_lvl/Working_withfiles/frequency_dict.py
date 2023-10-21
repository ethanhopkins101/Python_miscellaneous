#Description:
#1-Write a Python program that creates and prints a frequency dictionary of the words found in a text file.
#2-The keys of the dictionary should be the words in the file.
#3-The values should be their frequencies.
#4-You may assume that each line of the file only contains one word.

from collections import Counter
path=r'Beginner_lvl\Working_withfiles\text.txt'
file=open(path,mode='r')

list_a=[line.strip('\n') for  _,line in enumerate(file)]
dict_c=Counter(list_a)
print(dict_c)

file.close()