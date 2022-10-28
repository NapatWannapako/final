# Write a program to create a class called Student with the following attributes:
'''Follow this requirements:
1. Create a class called Student
2. Create 2 attributes: name, student_id
3. Create 2 methods: get_name(), get_student_id()
4. Create 2 objects: student1, student2
5. Print the name and student_id of student1 and student2
6. Print the type of student1 and student2
'''


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id


if __name__ == "__main__":
    student1 = Student("John", 1)
    student2 = Student("Mary", 2)
    print(student1.get_name(), student1.get_student_id())
    print(student2.get_name(), student2.get_student_id())
    print(type(student1), type(student2))
