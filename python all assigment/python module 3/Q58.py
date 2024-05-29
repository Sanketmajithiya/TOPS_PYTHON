# Q.58 Write a Python program to read a random line from a file. 
import random
def r_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(r_line('test.txt'))