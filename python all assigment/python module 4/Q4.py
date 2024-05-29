""" Q.4 Write a Python program to read first n lines of a file."""

n = int(input("Enter lines To read : "))
f = open("new_file.txt","r")
for i in range(n):
	print(f.readline())
