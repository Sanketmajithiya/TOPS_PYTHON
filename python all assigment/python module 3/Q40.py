# Q.40 Write a Python program to map two lists into a dictionary .

keys = ['a', 'b', 'c']
values = [1, 2, 3]
# Print the mapped dictionary directly using dictionary comprehension within the print statement
print("Mapped dictionary:", {k: v for k, v in zip(keys, values)})
