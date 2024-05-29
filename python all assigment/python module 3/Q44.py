# Q.44 Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
#Sample data: {'1': ['a','b'], '2': ['c','d']}
#Expected Output:
#ac ad bc bd 

from itertools import product

def all_combinations(dictionary):
    # Directly generate all combinations of letters and join each combination
    return [''.join(comb) for comb in product(*dictionary.values())]

data = {'1': ['a', 'b'], '2': ['c', 'd']}
print(" ".join(all_combinations(data)))
