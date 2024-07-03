# Q.11 Write a Python function that takes a list and returns a new list with unique elements of the first list. 


def unique_elements(input_list):
    return list(set(input_list))

original_list = [1, 2, 3, 3, 4, 5, 5, 6]
print("Original list:", original_list)
print("Unique list:", unique_elements(original_list))


