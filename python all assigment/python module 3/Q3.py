"""
Difference between append () and extend () methods? 
"""
# append():
# we can add new item in old list at the END as a single element.
my_list = [1,2,3]
my_list.append(["sanket","majithiya"])
print(my_list) # [1, 2, 3, ['sanket', 'majithiya']]

# extend():
# we can add all elements at the end of list
my_list.extend(([4,5],{1,2,3,1}))
print(my_list)
