# Q.12 Write a Python program to copy the contents of a file to another file. 



source_file = open('source.txt', 'r')
destination_file = open('destination.txt', 'w')

destination_file.write(source_file.read())

source_file.close()
destination_file.close()


