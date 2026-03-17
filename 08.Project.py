lines = []

with open("constitution.txt", "r") as file:
    for line in file:
        lines.append(line.rstrip())

while True:
    term = input("Enter search term: ").strip()
    if term == "":
        break

    i = 0
    found_any = False
    while i < len(lines):
        if term.lower() in lines[i].lower():
            found_any = True

            # Find start of section (move back to first blank line or start of file)
            start = i
            while start > 0 and lines[start-1].strip() != "":
                start -= 1

            # Find end of section (move forward to next blank line or end of file)
            end = i
            while end + 1 < len(lines) and lines[end+1].strip() != "":
                end += 1

            # Print section
            for j in range(start, end + 1):
                print(f"Line {j+1}: {lines[j]}")
            print()

            i = end + 1  # Move past the section so we don't print it twice
        else:
            i += 1
