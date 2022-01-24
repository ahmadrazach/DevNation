row = int(input("enter the height:"))
for i in range(row):  # using hill pattern
    for j in range(i, row):
        print(" ", end=" ")
    for j in range(i):
        print("#", end="")
    print()
