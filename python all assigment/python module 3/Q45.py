# Q.45 Write a Python program to find the highest 3 values in a dictionary.

my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 50, 'e': 40}
print("Highest 3 values:", sorted(my_dict.values(), reverse=True)[:3])
