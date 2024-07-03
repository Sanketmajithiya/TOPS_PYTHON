# Q.7 Write a Python program to remove duplicates from a list.

original_list = [1, 2, 3, 4, 2, 3, 5]
rem_dup_items = []
for i in original_list:
 if i not in rem_dup_items:
   rem_dup_items.append(i)
print(rem_dup_items)










