"""Write a Python program to count the number of characters (character frequency) in a string """
string = "python.program"

char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
