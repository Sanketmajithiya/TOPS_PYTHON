# Q.16 Write a Python program to check whether a list contains a sub list.


def contains_sublist(main_list, sublist):
    return any(main_list[i:i+len(sublist)] == sublist for i in range(len(main_list) - len(sublist) + 1))

print("Main list:", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Sublist:", [3, 4, 5])
print("Does the main list contain the sublist?", contains_sublist([1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5]))

