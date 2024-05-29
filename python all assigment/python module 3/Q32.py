# Q.32 Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 3, 'banana': 1, 'orange': 2}
print("Sorted dictionary (ascending):", dict(sorted(my_dict.items(), key=lambda x: x[1])))
print("Sorted dictionary (descending):", dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))
