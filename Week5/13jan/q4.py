# Q4
# Write a program that calculates the average of all elements in the following array/list

my_list = [1, 22, 32, 12, 55, 88, 76, 54, 2, 1, 22, 33, 44, 5, 6, 6, 7, 5, 0]
sum = 0
for i in range(len(my_list)):
    sum = sum+my_list[i]

print("Average of the numbers :", sum/len(my_list))
