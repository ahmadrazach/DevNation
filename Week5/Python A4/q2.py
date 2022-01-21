# Nested Loops
# take input of how long and wide the flag would be
flag_length = int(input("How long is your flag? - "))
flag_width = int(input("How wide is your flag? - "))
# take input of flag pole's length and width
flagpole_length = int(input("How long is your flagpole? - "))
flagpole_width = int(input("How wide is your flagpole? - "))

# make a function named rectangle(I,b)


def rectangle(l, b):
    #   loop untill the length of rectangle
    for i in range(l):
        #       loop untill wide of the rectangle
        for i in range(b):
            #           print("*",end="")
            print("*", end="")
        print()


# give flag length and breadth as arguments to the function
rectangle(flag_length, flag_width)
# give flagpole's length and width as arguments to the function
rectangle(flagpole_length, flagpole_width)
