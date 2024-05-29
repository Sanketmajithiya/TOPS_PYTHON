"""Q.9 Write a Python program to count the number of lines in a text file. """
filename = 'new_file.txt'  
with open(filename, 'r') as file:
    line_count = sum(1 for line in file)

print("Number of lines in the file:", line_count)
