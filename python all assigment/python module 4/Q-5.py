# Q.5 Write a Python program to read last n lines of a file. 

file_name = 'file_name.txt'

n = int(input("enter the number from last : "))
# n = 5 

with open(file_name, 'r') as file:
    lines = file.readlines()
    print(lines)
    last_n_lines = lines[-n:]

print(f"Last {n} lines of the file:")
for line in last_n_lines:
    print(line.strip())

