

path=r'C:\Users\mmopa\OneDrive\Documents\Git_General\Git_Python_problems_solutions\Beginner_lvl\Working_withfiles\text.txt'
file=open(path,mode='r')

n=2
list_a=[line.strip('\n') for _,line in enumerate(file.readlines())]
print('Last {} lines are: '.format(n))
print(list_a[-n:])

file.close()