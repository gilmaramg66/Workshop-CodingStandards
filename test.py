class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False
        self.letter_grade = "-"

    def add_grades(self, grade):
        if isinstance(grade, float) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Invalid grade. '{grade}' must be a float between 0 and 100.")

    def calc_average(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter_grade)


def startrun():
    a = Student("x", "")
    a.add_grades(100)
    a.add_grades("Fifty")  # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  # IndexError
    a.report()


startrun()
