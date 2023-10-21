#Description:
#1-Write a Python program that finds and prints the longest word in a text file.
#2-For this challenge, you may assume that the file only contains one word per line.

path=r'C:\Users\mmopa\OneDrive\Documents\Git_General\Git_Python_problems_solutions\Beginner_lvl\Working_withfiles\text.txt'
file=open(path,mode='r')

list_a=[line.strip('\n') for _,line in enumerate(file.readlines())]
longest_word=''
maxx=0
for i in list_a:
    if (len(i))>maxx:
        maxx=len(i)
        longest_word=i
print('Longest Word is: {} -------- with len of: {}'.format(longest_word,maxx))

file.close()