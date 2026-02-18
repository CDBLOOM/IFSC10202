first_number = float(input("Enter First Number: "))
enter_operator = input("Enter Operator (+, -, *, /): ")
second_number = float(input("Enter Second Number: "))

if enter_operator == "+":
   print(first_number + second_number)
elif enter_operator == "-":
    print(first_number - second_number)
elif enter_operator == "*":
    print(first_number * second_number)
elif enter_operator == "/":
    if second_number != 0:
        print(first_number / second_number)
else:
    print("Invalid Operator, try again!!!")
