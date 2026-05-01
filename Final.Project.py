class Employee:
    def __init__(self, emp_num, first, last, address, city, state, zip_code):
        self.emp_num = int(emp_num)
        self.first = first
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

class EmployeeList:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []

    def find_employee(self, emp_num):
        for i, emp in enumerate(self.employees):
            if emp.emp_num == emp_num:
                return i
        return -1

    def next_employee_number(self):
        if not self.employees:
            return 1
        return self.employees[-1].emp_num + 1

    def read_employee_file(self):
        self.employees = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 7:
                        emp = Employee(*[x.strip() for x in data])
                        self.employees.append(emp)
        except FileNotFoundError:
            pass

    def write_employee_file(self):
        with open(self.filename, "w") as file:
            for emp in self.employees:
                file.write(f"{emp.emp_num},{emp.first},{emp.last},{emp.address},{emp.city},{emp.state},{emp.zip_code}\n")

    def display_employee_list(self):
        print("\nEmployee Number  First Name  Last Name  Address  City  State  Zip")
        print("-" * 70)
        for emp in self.employees:
            print(f"{emp.emp_num:<15}{emp.first:<12}{emp.last:<12}{emp.address:<12}{emp.city:<12}{emp.state:<8}{emp.zip_code:<10}")

    def add_employee(self, first, last, address, city, state, zip_code):
        emp_num = self.next_employee_number()
        emp = Employee(emp_num, first, last, address, city, state, zip_code)
        self.employees.append(emp)
        print("Employee Added")

    def update_employee(self, emp_num, first, last, address, city, state, zip_code):
        index = self.find_employee(emp_num)
        if index == -1:
            print("Employee not found")
            return

        emp = self.employees[index]
        emp.first = first
        emp.last = last
        emp.address = address
        emp.city = city
        emp.state = state
        emp.zip_code = zip_code

    def delete_employee(self, emp_num):
        index = self.find_employee(emp_num)
        if index == -1:
            print("Employee not found")
            return
        del self.employees[index]
        print("Employee Deleted")

def main():
    emp_list = EmployeeList("Final Project Employees.txt")
    emp_list.read_employee_file()

    while True:
        print("\n(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit")

        choice = input("\nEnter Selection: ").upper()

        if choice == "A":
            first = input("Enter First Name: ")
            last = input("Enter Last Name: ")
            address = input("Enter Address: ")
            city = input("Enter City: ")
            state = input("Enter State: ")
            zip_code = input("Enter Zip: ")
            emp_list.add_employee(first, last, address, city, state, zip_code)

        elif choice == "D":
            emp_num = int(input("Enter Employee Number: "))
            emp_list.delete_employee(emp_num)

        elif choice == "C":
            emp_num = int(input("Enter Employee Number: "))
            index = emp_list.find_employee(emp_num)

            if index == -1:
                print("Employee not found")
                continue

            emp = emp_list.employees[index]

            while True:
                print("\n(F)irst Name")
                print("(L)ast Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack to Main Menu")

                sub = input("\nEnter Selection: ").upper()

                if sub == "F":
                    emp.first = input("Enter First Name: ")
                elif sub == "L":
                    emp.last = input("Enter Last Name: ")
                elif sub == "A":
                    emp.address = input("Enter Address: ")
                elif sub == "C":
                    emp.city = input("Enter City: ")
                elif sub == "S":
                    emp.state = input("Enter State: ")
                elif sub == "Z":
                    emp.zip_code = input("Enter Zip: ")
                elif sub == "B":
                    break

        elif choice == "P":
            emp_list.display_employee_list()

        elif choice == "S":
            emp_list.write_employee_file()
            print("Changes Saved")

        elif choice == "Q":
            print("Good-bye")
            break


if __name__ == "__main__":
    main()