#Description:
#1-Write a Python program that implements the Binary Search algorithm recursively.
#2-The function should search for an element in a list or sequence and return its index.
#3-If the element is not found, the value returned should be -1.

def binary_search(l1,element):
    if not l1:
        print('-1')
    elif l1[-1]==element:
        print(len(l1)-1)
    else:
        binary_search(l1[:-1],element)

l1=[4,5,6,2]
print(binary_search(l1,3))