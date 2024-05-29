# Q.7 Write a Python program to read a file line by line store it into a variable.

file = open('output.txt', 'r')

lines = []

for line in file:
    lines.append(line.strip())
file.close()

print(lines)