# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    # loop till all the path
    for i in range(steps):
        if path[i] == "D":
            count -= 1
        else:
            count += 1

    return int(count)


print(countingValleys(8, "UDDUDUU"))
