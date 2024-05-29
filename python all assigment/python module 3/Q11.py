# Q.11 Write a Python function that takes a list and returns a new list with unique elements of the first list. 


# def unique_elements(input_list):
#     return list(set(input_list))

# original_list = [1, 2, 3, 3, 4, 5, 5, 6]
# print("Original list:", original_list)
# print("Unique list:", unique_elements(original_list))
# # 


# Write a Python function that takes a list and returns a new list with unique elements of the first list. 

def unique_elements(input_list):
    return list(set(input_list))

original_lits = [1,2,3,4,5,6,5]
print("original lits:",original_lits)
print("unique list:",unique_elements(original_lits))