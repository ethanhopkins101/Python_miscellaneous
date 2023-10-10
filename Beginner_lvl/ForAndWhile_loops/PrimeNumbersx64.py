#Description:
#1-Write a Python program that checks if a number is prime or not.
#2-If the number is prime, it should print "Prime".
#3-If the number is not prime, it should print "Not prime".
#A prime number is only divisible by 1 and by itself. It is not the product of two smaller natural numbers.

number_a=11
x=2
notPrime=False
if number_a in [0,1]:
    print("Not prime")
else:

    while x<=number_a/2:
        if number_a%x==0:
            notPrime=True
            break
        x+=1
    print('Not prime' if notPrime else 'Prime')