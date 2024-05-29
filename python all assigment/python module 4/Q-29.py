# Q.29 What relationship is appropriate for Student and Person? 

"""In Python, if you're asking about representing the relationship between a student and a person in terms of 
   programming, you might consider using object-oriented programming (OOP) concepts. Here's a simple example using
   classes:
"""
class person:
    def __init__(self, name, age):
        self.n = name
        self.ag = age

    def introduce(self):
        print(f"my name is {self.n} and I am {self.ag} years old.")


class Student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.n} with student ID {self.student_id} is studying.")


person1 = person("sanket", 22)
person1.introduce()

student1 = Student("VK", 20, "12345")
student1.introduce()  
student1.study()
