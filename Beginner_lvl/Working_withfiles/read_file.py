#Description:
#1-Write a Python program that reads a text file and saves its content line by line to a list called file_content.
#2-The list should contain strings that represent each line of the text file.
#3-The program should print the resulting list.

path=r'C:\Users\mmopa\OneDrive\Documents\Git_General\Git_Python_problems_solutions\Beginner_lvl\Working_withfiles\text.txt'

file=open(path,mode='r')
for line in file.readlines():
    print(line)

file.close()