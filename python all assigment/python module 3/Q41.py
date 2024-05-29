# Q.41 Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

from collections import Counter

def combine_dicts(d1, d2):
    combined_dict = Counter(d1)
    combined_dict.update(d2)
    return combined_dict

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Print the combined dictionary directly within the print statement
print("Combined dictionary:", combine_dicts(d1, d2))
