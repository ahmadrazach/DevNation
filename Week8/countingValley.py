# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    unit = 0
    valleys_traversed = 0
    # loop till all the path
    for i in path:
        # for i in range(steps):

        #     if path[i] == "D":
        if i == "D":
            #         unit -= 1
            unit -= 1
        #     else:
        else:
            #         unit += 1
            unit += 1
        if unit == 0 and i == "U":
            valleys_traversed += 1

    return(int(valleys_traversed))


print(countingValleys(8, "DUDDDUUDUU"))
