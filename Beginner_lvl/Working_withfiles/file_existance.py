#Description:
#1-Write a Python program that checks if a file exists in the specified path or not.
#2-If it exists, print "The file <file_name> exists"
#3-If it doesn't, print "The file <file_name> doesn't exist"
#4-The file name could also be an absolute path to the file.

path=r'Beginner_lvl\Working_withfiles\alphh.txt'
try:
    file=open(path,mode='r')
    print('{} exists'.format(file.name))
except FileNotFoundError:
    print('{} does not exist'.format(path))