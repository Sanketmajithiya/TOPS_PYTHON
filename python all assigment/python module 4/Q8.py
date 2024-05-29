""" Q.8 Write a python program to find the longest words. """
filename = 'new_file.txt'  
with open(filename, 'r') as file:
    words = file.read().split()  
    longest_length = max(len(word) for word in words) 
    longest_words = [word for word in words if len(word) == longest_length]  
print("Longest :", longest_words)
