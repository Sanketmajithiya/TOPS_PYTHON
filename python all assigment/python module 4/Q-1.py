# Q.1 What is File function in python? What is keywords to create and write file.
'''
The file function in Python is a built-in function that takes a filename as an argument and returns a file object. 
The file object can then be used to read, write, or append data to the file.
The file function takes two arguments: the filename and the mode. The mode argument specifies how the file should be opened.
'''

# To create file:
# open('file_name.txt', 'x')

# To Write file:
file = open('file_name.txt', 'w') 
file.write("this is a python programming, and i am going to learn it.\n")
file.write("this is a python programming, and i am going to learn it.\n")
file.write("this is a python programming, and i am going to learn it.\n")
file.write("this is a python programming, and i am going to learn it.\n")
file.write("this is a python programming, and i am going to learn it.\n")
file.write("this is a python programming, and i am going to learn it.\n" * 50)
file.close()


# open("test.txt",'x')

file=open('test.txt','w')

file.write("this is a test file, for python programming file handling \n"*10)

file.close()