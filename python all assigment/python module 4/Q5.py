""" Q.5 Write a Python program to read last n lines of a file. """
myfile = open("new_file.txt","r")

lines = myfile.readlines()
last_l = lines[-1]
print(last_l)

