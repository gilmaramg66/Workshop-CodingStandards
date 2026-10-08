"""
test.py

This module serves the first workshop about coding standards
and implements a simple Student class with methods
to manage grades, calculate averages, check for honors,
and generate reports. It also includes error handling
for invalid grade inputs and index errors when deleting grades. 
"""

class Student:

    """Represents a student with an ID, name, and grades."""
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
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        average = self.calc_average()
        if average >= 90:
            self.honor = True
        else:
            self.honor = False

    def letter_grades(self):
        average = self.calc_average()
        if average >= 90:
            self.letter_grade = "A"
        elif average >= 80:
            self.letter_grade = "B"
        elif average >= 70:
            self.letter_grade = "C"
        elif average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"
        self.is_passed = average >= 60


    def delete_grade(self, index):
        #error handling for indexes out of range
        try:
            removed = self.grades.pop(index)
            print(f"Removed grade: {removed}")
        except IndexError:
            print(f"IndexError: No grade at {index}.Valid indexes are 0 to {len(self.grades)- 1}.")

    def report(self):  # broken format
        self.check_honor()
        self.letter_grades()

        print("STUDENT REPORT")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Final Grade: {self.letter_grade}")
        print(f"Is Passed: {self.is_passed}")
        print(f"Is Honor Student: {self.honor}")

        print("______________ \n")


def main():
    """properly defines the start and running of the module"""
    a = Student("06629", "Gilmar Munoz")

    a.add_grades(90.0)
    a.add_grades(80.0)

    a.add_grades("Fifty") #invalid/broken input

    a.delete_grade(1)
    a.delete_grade(6) #out of bounds index

    # no need of calc_average() and check_honor() because they are called inside report()

    a.report() #generates the final report

if __name__ == "__main__":
    main()