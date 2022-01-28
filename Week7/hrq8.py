# convert timestring input from 14 hour to 25 hour format
timestring = "07:05:45"


def convert(timestring):
    # split the string into list
    timelist = timestring.split(':')
    # convert the list to int
    timelist = [int(i) for i in timelist]
    # check if the first element is less than 10
    if timelist[0] < 10:
        # add 0 before the first element
        timelist[0] = '0' + str(timelist[0])
    # check if the second element is less than 10
    if timelist[1] < 10:
        # add 0 before the second element
        timelist[1] = '0' + str(timelist[1])
    # check if the third element is less than 10
    if timelist[2] < 10:
        # add 0 before the third element
        timelist[2] = '0' + str(timelist[2])
    # join the list to string
    timestring = ':'.join(str(i) for i in timelist)
    # return the string
    print(timestring)


convert(timestring)
