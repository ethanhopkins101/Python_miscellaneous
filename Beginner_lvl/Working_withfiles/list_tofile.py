#Description:
#1-Write a Python program that writes the elements of a list to the file denoted by the variable file.
#2-Each element should be written on a separate line.
#3-The file should be new or its existing content must be replaced by this new content.

path=r'Beginner_lvl\Working_withfiles\write.txt'
file=open(path,mode='w')

list_a=['Hello','World','Currently','Typing','In','A','File']

for i in list_a:
    file.writelines(i+'\n')