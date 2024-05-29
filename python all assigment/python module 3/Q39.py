# Q.39 Write a Python script to merge two Python dictionaries .


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dictionaries using dictionary unpacking
merged_dict = {**dict1, **dict2}
print("Merged dictionary using dictionary unpacking:", merged_dict)
