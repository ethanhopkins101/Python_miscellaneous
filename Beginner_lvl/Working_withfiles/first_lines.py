#Description:
#1-Write a Python program that reads a text file and prints the first n lines of the file.
#2-The value of n should be entered by the user.
#3-If the value of n is greater than the total number of lines in the file, print
#"Please enter a value for n. The file has <num_lines> lines".

path=r"C:\Users\mmopa\OneDrive\Documents\Git_General\Git_Python_problems_solutions\Beginner_lvl\Working_withfiles\text.txt"
file=open(path,mode='r')

n=3
list_a=[line.strip('\n') for _,line in enumerate(file.readlines())]
print('first {} lines are :'.format(n))
print(list_a[:n])


file.close()