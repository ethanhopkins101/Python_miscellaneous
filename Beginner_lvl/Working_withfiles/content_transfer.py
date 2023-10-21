#Description:
#1-Write a Python program that copies the content of a file to another file.
#2-If the new file doesn't exist, the program should create it.


path1=r'Beginner_lvl\Working_withfiles\text.txt'
file1=open(path1,mode='r')

path2=r'Beginner_lvl\Working_withfiles\write.txt'
file2=open(path2,mode='w')

file2.writelines(file1.readlines())

file1.close()
file2.close()

