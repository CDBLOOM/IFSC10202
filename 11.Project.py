class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        total = 0
        count = 0

        for g in self.Grades:
            if g != "":
                total += float(g)
                count += 1

        if count == 0:
            return 0

        return total / count

    def TotalAverage(self):
        total = 0

        for g in self.Grades:
            if g == "":
                total += 0
            else:
                total += float(g)

        if len(self.Grades) == 0:
            return 0

        return total / len(self.Grades)

    def LetterGrade(self):
        avg = self.TotalAverage()

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        self.Studentlist.append(Student(firstname, lastname, tnumber))

    def find_student(self, tnumber):
        i = 0
        while i < len(self.Studentlist):
            if self.Studentlist[i].TNumber == tnumber:
                return i
            i += 1
        return -1

    def print_student_list(self):
        print(f"{'First':>12}{'Last':>12}{'ID':>12}{'Running':>12}{'Semester':>12}{'Letter':>12}")
        print(f"{'Name':>12}{'Name':>12}{'Number':>12}{'Average':>12}{'Average':>12}{'Grade':>12}")
        print("-" * 72)

        for s in self.Studentlist:
            print(f"{s.FirstName:>12}{s.LastName:>12}{s.TNumber:>12}"
                  f"{s.RunningAverage():>12.2f}{s.TotalAverage():>12.2f}{s.LetterGrade():>12}")

    def add_student_from_file(self, filename):
        file = open(filename, "r")

        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 3:
                self.add_student(parts[0], parts[1], parts[2])

        file.close()

    def add_scores_from_file(self, filename):
        file = open(filename, "r")

        for line in file:
            parts = line.strip().split(",")

            tnumber = parts[0]
            score = ""

            if len(parts) > 1:
                score = parts[1]

            index = self.find_student(tnumber)

            if index != -1:
                self.Studentlist[index].Grades.append(score)

        file.close()

students = StudentList()

students.add_student_from_file("11.Project Students.txt")
students.add_scores_from_file("11.Project Scores.txt")

students.print_student_list()
