# Write a program to create a class called Student with the following attributes:
'''Follow this requirements:
1. Create a class called Student
2. Create 2 attributes: name, student_id
3. Create 2 methods: get_name(), get_student_id()
4. Create subclass called DMEStudent
5. Create 3 attributes: major, courses, gpa
6. Create 3 methods: get_major(), get_courses(), get_gpa()
7. Create subclass called CoEStudent
8. Create 3 attributes: major, courses, gpa
9. Create 3 methods: get_major(), get_courses(), get_gpa()
10. Create 2 objects: student1, student2
11. Print the name and student_id of student1 and student2
'''


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id


class DMEStudent(Student):
    def __init__(self, name, student_id, major, courses, gpa):
        super().__init__(name, student_id)
        self.major = major
        self.courses = courses
        self.gpa = gpa

    def get_major(self):
        return self.major

    def get_courses(self):
        return self.courses

    def get_gpa(self):
        return self.gpa


class CoEStudent(Student):
    def __init__(self, name, student_id, major, courses, gpa):
        super().__init__(name, student_id)
        self.major = major
        self.courses = courses
        self.gpa = gpa

    def get_major(self):
        return self.major

    def get_courses(self):
        return self.courses

    def get_gpa(self):
        return self.gpa


if __name__ == "__main__":
    student1 = DMEStudent(
        "John", 6430401111, "DME", ["DME101", "DME102", "DME103"], 3.5)
    student2 = CoEStudent(
        "Mary", 6430401112, "CoE", ["CoE101", "CoE102", "CoE103"], 3.8)
    print(student1.get_name(), student1.get_student_id())
    print(student2.get_name(), student2.get_student_id())
    print(student1.get_major(), student1.get_courses(), student1.get_gpa())
    print(student2.get_major(), student2.get_courses(), student2.get_gpa())
