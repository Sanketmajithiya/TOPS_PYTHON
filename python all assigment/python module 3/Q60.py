# Q.60 Write a Python program to calculate the area of a trapezoid 

def trapezoid_area(a, b, h):
    return 0.5 * (a + b) * h
side_a, side_b, height = 5, 7, 4
print("Area of the trapezoid:", trapezoid_area(side_a, side_b, height))
