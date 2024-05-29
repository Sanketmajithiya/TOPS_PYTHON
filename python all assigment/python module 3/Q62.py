# Q.62 Write a Python program to calculate surface volume and area of a cylinder.
import math

cylinder_volume = lambda radius, height: math.pi * radius**2 * height
cylinder_surface_area = lambda radius, height: 2 * math.pi * radius * (radius + height)

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

print("The volume of the cylinder is:", cylinder_volume(radius, height))
print("The surface area of the cylinder is:", cylinder_surface_area(radius, height))
