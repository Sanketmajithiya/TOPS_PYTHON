# Q.61 Write a Python program to calculate the area of a parallelogram.

print("The area of the parallelogram is:", (lambda base, height: base * height)(
    float(input("Enter the length of the base of the parallelogram: ")),
    float(input("Enter the height of the parallelogram: "))
))
