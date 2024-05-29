# Q.27 Write a Python program to find the repeated items of a tuple.

from collections import Counter
print("Repeated items:", [item for item, count in Counter((1, 2, 3, 2, 4, 3, 5, 6, 1)).items() if count > 1])

