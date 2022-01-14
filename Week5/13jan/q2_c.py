# Q2_c
# print that !
# 1010101
#  10101
#   101
#    1

#rows = input("Please enter the no. of rows :")
rows = 4

for i in range(4):  # reverse hill pattern
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i, 4-1):
        if j % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    for j in range(i, 4):
        if j % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
