#Description:
#1-Write a Python program that counts the number of characters in a file.
#2-Count all the characters in the file, including commas and quotes.
#3-Do not count spaces and remove \n (new line) characters.

path=r'Beginner_lvl\Working_withfiles\text.txt'
file=open(path,mode='r')

list_a=[word.strip('\n').replace(' ','') for _,word in enumerate(file.read())]
resulting_str=''.join(list_a)

print('Number of chars in the given file is: {}'.format(len(resulting_str)))

file.close()