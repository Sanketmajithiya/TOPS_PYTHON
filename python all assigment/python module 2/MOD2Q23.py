""" Q.23 Write a Python function to insert a string in the middle of a string."""
str1 = "hello how are you"
lefts = str1[:6]
right = str1[5:]
add = input("enter your name: ")
new_string = lefts + add + right
print(" ",new_string)