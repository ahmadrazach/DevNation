# Q2
# 1st part
# num = input("Input a number")
# num = int(num)
# i = 1
# while(i <= num):
#     for x in range(0, i):
#         print("*", end=" ")
#     print("")
#     i = i+1


# part
num = 3
num = int(num)

# loop to range
for i in range(num):

    # print space before number
    x = 1
    while x < num:
        print(" ", end="")
        x = x+1

    print("*", end="")
    while x > 1:
        print(" ", end="")
        x = x-1
    print(" ")
#    *
#   ***
#  *****
#   ***
#    *
# 5 0,5
