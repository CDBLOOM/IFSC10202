with open("09.Project Distances.csv", "r") as file:
    table = []
    for line in file:
        line = line.strip()
        row = line.split(",")
        table.append(row)

# print table with alignment
for row in table:
    for item in row:
        print(f"{item:>10}", end="")
    print()

from_city = input("Enter From City: ")
to_city = input("Enter To City: ")

r_index = -1
c_index = -1

# find row (from city)
i = 1
while i < len(table):
    if table[i][0] == from_city:
        r_index = i
        break
    i += 1

# find column (to city)
j = 1
while j < len(table[0]):
    if table[0][j] == to_city:
        c_index = j
        break
    j += 1

# output results
if r_index == -1:
    print("Invalid From City")
elif c_index == -1:
    print("Invalid To City")
else:
    distance = table[r_index][c_index]
    print(from_city, "to", to_city, "-", distance, "miles")