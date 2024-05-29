# Q.3 Differentiate between append () and extend () methods? 

""" 1 append(): This method adds a single element to the end of the list."""
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  
"""2 extend(): This method adds elements from an iterable (such as a list, tuple, or another iterable) to the end of the list. It essentially concatenates the iterable with the list."""

my_list = [1, 2, 3]
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)  





















