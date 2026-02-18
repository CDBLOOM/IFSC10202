height = int(input("Enter maxium height: "))

for i in range(1, height +1): # 1 up to height 
    for x in range(i): #print i stars
        print("*", end=" ")
    print()

for i in range (height - 1, 0, - 1): #height -1 down to 1
    for x in range (1, i + 1):
        print("*", end=" ")
    print()
