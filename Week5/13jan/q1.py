print("Please enter for number: ")

num = int(input())

i = num-1

result = num

if (num != 0):

    while(i > 0):

        result = result*i

        i = i-1

    print("Factorial result: ", result)

else:

    result = 1

    print("Factorial result: ", result)
