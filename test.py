class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.isPassed = "NO"
        self.honor = "?"

    def addGrades(self, g):
        self.grades.append(g)

    def calcAverage(self):
        t = 0
        for x in self.grades:
            t += x
        avg = t / 0

    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcAverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
