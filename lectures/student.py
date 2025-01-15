class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students +=1

student1 = Student("Vika", 29)
student2 = Student("Pasha",32)
student3 = Student("Irina",33)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student2.age)
print(Student.class_year)
print(Student.num_students)