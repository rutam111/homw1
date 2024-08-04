from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = 0

    @abstractmethod
    def get_grade(self):
        pass

    @abstractmethod
    def set_grade(self, new_grade):
        pass

class Biology(Student):
    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
        else:
            print("Grade must be between 0 and 100!")

class Math(Student):
    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
        else:
            print("Grade must be between 0 and 100!")

bio_student = Biology("Alice", 101)
bio_student.set_grade(85)
print(f"{bio_student.name}'s Biology grade: {bio_student.get_grade()}")

math_student = Math("Bob", 102)
math_student.set_grade(92)
print(f"{math_student.name}'s Math grade: {math_student.get_grade()}")
