row = int(input("enter the height:"))
for i in range(row-1):  # using hill pattern
    for j in range(i, row):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(row):  # reverse hill pattern
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, row-1):
        print("*", end=" ")
    for j in range(i, row):
        print("*", end=" ")
    print()
