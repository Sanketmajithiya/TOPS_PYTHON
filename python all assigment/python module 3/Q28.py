# Q.28 Write a Python program to remove an empty tuple(s) from a list of tuples.

list_of_tuples = [(1, 2), (), (3, 4), (), (5, 6), ()]
print("List after removing empty tuples:", [tup for tup in list_of_tuples if tup])
