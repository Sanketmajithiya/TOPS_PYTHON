""" Q.3 Write a Python program to get the Fibonacci series of given range """
a,b = 0,1
num = int(input("please enter num :"))
if (num == 1):
    print(a)
else:
    for i in range(1,num +1):
     c = a + b
     a = b
     b = c 
     print(c)
