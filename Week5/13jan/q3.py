# Q3
# Write a program that takes integer inputs from the user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.
sum = 0
product = 1
iteration = 0
print("Enter the numbers and input q for the results")
while 1:
    num = input()  # taking input and converting to integers
    if num == 'q':    # checking if user inputs the q to break the loop
        break
    else:
        sum = sum+int(num)
        product = product*int(num)
        iteration = iteration+1

print("Average  of all no.s :", sum/iteration)
print("Product of all no.s:", product)
