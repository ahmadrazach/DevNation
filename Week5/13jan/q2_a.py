# Q2
# 1st part
num = input("Input a number")
num = int(num)
i = 1
while(i <= num):
    for x in range(0, i):
        print("*", end=" ")
    print("")
    i = i+1
