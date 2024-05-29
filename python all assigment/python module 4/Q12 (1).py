"""Q.12 Write a Python program to copy the contents of a file to another file. """

with open('myfile.txt','r') as firstfile, open('new_file.txt','a') as secondfile: 
	
	for line in firstfile: 
			
			secondfile.write(line)
