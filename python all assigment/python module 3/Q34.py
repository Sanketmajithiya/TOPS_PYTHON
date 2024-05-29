# Q.34 Write a Python script to check if a given key already exists in a dictionary.

my_dict = {1:10 , 2:20 ,3:'sanket',4:40,5:50,6:'xyz'}
def check_value(value):
    if value in my_dict:
        print(" already exists....!")
    else:
        print(" key value not present in dict...!")
        check_value(3)
        check_value(6)










































# # Example dictionary
# example_dict = {'a': 1, 'b': 2, 'c': 3}

# # Key to check
# key_to_check = 'b'

# # Check if key exists using the 'in' keyword
# print(f"The key '{key_to_check}' {'exists' if key_to_check in example_dict else 'does not exist'} in the dictionary.")

# # Check if key exists using the 'get()' method
# print(f"The key '{key_to_check}' {'exists' if example_dict.get(key_to_check) is not None else 'does not exist'} in the dictionary.")
