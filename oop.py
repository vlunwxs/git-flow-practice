class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Subject:
    def _init_(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Diary:
    def _init_(self, student):
        self.student = student
        self.subjects = []
        self.grades = {}

    def add_subject(self, subject):
        self.subjects.append(subject)

    def record_grade(self, subject, grade):
        if subject in self.subjects:
            if subject not in self.grades:
                self.grades[subject] = []
            self.grades[subject].append(grade)

    def get_grades(self, subject):
        if subject in self.grades:
            return self.grades[subject]
        else:
            return []


student1 = Student("Lera", 18)
subject1 = Subject("Math")
subject2 = Subject("History")
diary1 = Diary(student1)


diary1.add_subject(subject1)
diary1.add_subject(subject2)

diary1.record_grade(subject1, 90)
diary1.record_grade(subject1, 95)
diary1.record_grade(subject2, 85)


print(f"Student: {student1.get_name()}, Age: {student1.get_age()} years old")
print(f"Grades in {subject1.get_name()}: {diary1.get_grades(subject1)}")
print(f"Grades in {subject2.get_name()}: {diary1.get_grades(subject2)}")