# Q.11 Write a Python program to write a list to a file. 


file = open('output_list.txt', 'w')

name_file = ["Vaman ", "chaman ", "baman ", "magan ", "kaman ", "ghaman ", "saman ", "gagan ", "raman ", "taman ", "iman ", "fagan "]

for names in name_file:
    file.write(names + '\n') 

file.close()