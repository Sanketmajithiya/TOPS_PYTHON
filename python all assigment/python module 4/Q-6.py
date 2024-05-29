#  Q.6 Write a Python program to read a file line by line and store it into a list.

file = open("file_name.txt", "r")
lines = file.readlines()
print(lines)

"""

['this is a python programming, and i am going to learn it.1\n', 'this is a python programming, and i am going to learn it.2\n', 'this is a python programming, and i am going to learn it.23\n', 'this is a python programming, and i am going to learn it.345\n', 'this is a python programming, and i am going to learn it.53413\n', 'this is a python programming, and i am going to learn it.56421\n', 'this is a python programming, and i am going to learn it.9+465321\n', 'this is a python programming, and i am going to learn it.798654\n', 'this is a python programming, and i am going to learn it.6543\n', 'this is a python programming, and i am going to learn it.8797\n', 'this is a python programming, and i am going to learn it654.\n', 'this is a python programming, and i am going to learn it.654\n', 'this is a python programming, and i am going to learn it.6554\n', 'this is a python programming, and i am going to learn it.654\n', 'this is a python programming, and i am going to learn it.5667\n', 'this is a python programming, and i am going to learn it.21\n', 'this is a python programming, and i am going to learn it.213']

"""
