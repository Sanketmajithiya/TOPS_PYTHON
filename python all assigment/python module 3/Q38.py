# Q.38 Write a Python program to check multiple keys exists in a dictionary.

def check_keys_exist(keys, dictionary):
    return all(key in dictionary for key in keys)

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b', 'd']
print("All keys exist in the dictionary." if check_keys_exist(keys_to_check, my_dict) else "One or more keys do not exist in the dictionary.")
