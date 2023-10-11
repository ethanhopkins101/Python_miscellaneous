#Description:
#1-Write a Python program that finds the sum of a list (or tuple) of numbers recursively.
#2-Print the total sum.
#3-If the list (or tuple) is empty, print 0.

def sum_list(list_a):
    if  len(list_a)==1:
        return list_a[0]
    else:
        return list_a[len(list_a)-1]+sum_list(list_a[:-1])
print(sum_list([4,5,8]))