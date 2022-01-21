# Collatz Conjecture


# take a postive integer input
number = int(input("Please enter a number : "))

if number > 0:
    print("Valid Number")
    chain_length = 1
    # repeat the loop untill it met the number 1
    print("The collatz chain is : ", number, end=" - ")
    while number != 1:
        # if number is odd:
        if number % 2 == 1:
            # multiply it by 3 add 1 (3n+1)
            number = ((3*number)+1)
            print(int(number), end=" - ")
        # if number is even:
        else:
            #  divide it by 2 (n/2)
            number = number/2
            print(int(number), end=" - ")
        chain_length += 1
    # print length of the chain
    print("\nColltz chain length: ", chain_length)
else:
    print("Invalid number")
