"""Q.7 Write a Python program to read a file line by line store it into a variable. """
def file_read(name):
        with open (name, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('new_file.txt')
