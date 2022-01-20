string = input("Enter a string")


def ascii_sum(string):  # function of ASCII sum
    sum = 0
    for i in string:
        sum = sum+ord(i)
        print(i)
    print(sum)


def ascii_sum_odd(string):  # function of ASCII sum odd
    sum = 0
    for i in range(1, len(string)+1):
        if i % 2 == 1:
            sum = sum+ord(string[i-1])

    print("Sum of odd numbers : ", sum)


def ascii_sum_even(string):  # function of ASCII sum even
    sum = 0
    for i in range(1, len(string)+1):
        if i % 2 == 0:
            sum = sum+ord(string[i-1])

    print("Sum of even numbers : ", sum)


ascii_sum(string)
ascii_sum_odd(string)
