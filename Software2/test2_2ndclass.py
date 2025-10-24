class Student:
    def __init__(self, name,gender, answer="present teacher" ):
        self.name = name
        self.gender = gender
        self.answer = answer

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
        print(self.name+" teaches IT")

    def add_student(self, student):
        self.students.append(student)
        print(student.name, student.answer)
        return

    def remove_student(self, student):
        self.students.remove(student)
        print(student.name+" is absent.")
        return


student1 = Student("Sujal", "Male")
student2 = Student("Princess", "Female")
student3 = Student("Blowman", "Male")

teacher = Teacher("Mr. President")
teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student3)

teacher.remove_student(student1)