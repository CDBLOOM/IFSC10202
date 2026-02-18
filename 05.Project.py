start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Special Numbers between", start, "and", end)

# Loop through every number in the range
for number in range(start, end +1):

# Count the number of digits
    x = number
    digit_count = 0 

    if x == 0:
        digit_count = 1
    else:
        while x > 0:
            x = x // 10
            digit_count += 1

    # Calculating sum of digits raised to power of the amount of digits
    x = number
    total = 0
    while x > 0:
        digit = x % 10
        total += digit ** digit_count
        x = x // 10 

        if total == number:
            print(number)

