# Lucky 7 in LUDO
import random
# ask user how may times the six-sided dice rolled
roll_times = int(input("How many times would like to roll the dice? - "))

#   for loop to run till the the times
for i in range(roll_times):
    sum = 0
#   for loop to run 2 times
    for j in range(2):
        no = random.randint(1, 6)
        sum += no
        print(j+1, "st value :", no)
    print("Dice roll", i+1, "sum : ", sum)
