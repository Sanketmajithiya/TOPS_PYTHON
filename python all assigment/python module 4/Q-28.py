# Q.28 What relationship is appropriate for Course and Faculty? 

"""In Python, you can establish a relationship between a Course and a Faculty using various methods 
depending on the requirements of your application. One common approach is to use object-oriented programming
 concepts like composition or aggregation."""
class faculty:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_name, faculty):
        self.course_name = course_name
        self.faculty = faculty


faculty1 = faculty("sanket", "python_lacture")
course1 = Course("Python Programming", faculty1)

print(f"Course: {course1.course_name}")
print(f"Faculty: {course1.faculty.name}")
print(f"Department: {course1.faculty.department}")
