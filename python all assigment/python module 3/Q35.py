# Q.35 How Do You Traverse Through A Dictionary Object In Python?.
""" in python,you can traverse throungh a dictionary using various method . Here are some common ways to iterate through dictionary:
using a for loop: 
you can use a for loop to iterate over the keys of the dictionary and access corresponding values. """

""" using items ()method : The items() method returns a view object that displays a list of a dictionary's
key-value tuple pairs. you can then iterate over these pairs directly."""

my_dict = {'a':1,'b':2,'c':3}

for key,value in my_dict.items():
    print(key,value)

