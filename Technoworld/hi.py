class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Grade:", self.grade)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
grade = input("Enter your grade: ")

s1 = Student(name, age, grade)

s1.display_info()

