# Q.23 Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 

class rectangle:
    def __init__(self, length, width):
        self.len = length
        self.wid = width

    def area(self):
        return self.len * self.wid

rectangle = rectangle(8, 5)

area_1 = rectangle.area()
print("Area of the rectangle:", area_1)