class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname.strip()
        self.LastName = lastname.strip()
        self.TNumber = tnumber.strip()
        self.Grades = scores

    def RunningAverage(self):
        valid = [float(s) for s in self.Grades if s != ""]
        if len(valid) == 0:
            return 0
        return sum(valid) / len(valid)

    def TotalAverage(self):
        total = 0
        count = len(self.Grades)

        for s in self.Grades:
            if s == "":
                total += 0
            else:
                total += float(s)

        if count == 0:
            return 0

        return total / count

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


def load_students(filename):
    students = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")

            firstname = parts[0]
            lastname = parts[1]
            tnumber = parts[2]
            scores = parts[3:]

            student = Student(firstname, lastname, tnumber, scores)
            students.append(student)

    return students


def print_report(students):
    print(f"{'First':>10}{'Last':>13}{'ID':>13}{'Running':>13}{'Semester':>13}{'Letter':>10}")
    print(f"{'Name':>10}{'Name':>13}{'Number':>13}{'Average':>13}{'Average':>13}{'Grade':>10}")
    print("-" * 72)

    for s in students:
        print(f"{s.FirstName:>10}{s.LastName:>13}{s.TNumber:>13}"
              f"{s.RunningAverage():13.2f}"
              f"{s.TotalAverage():13.2f}"
              f"{s.LetterGrade():>10}")


def main():
    students = load_students("StudentScores.txt")
    print_report(students)


if __name__ == "__main__":
    main()