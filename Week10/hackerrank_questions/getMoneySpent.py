def getMoneySet(keyboards, drives, b):
    # write code
    # max each list to save all the max elements
    max_each_with_keyboards = []
    # for loop till the keyboards
    for kb_value in keyboards:
        # sum list to take a keyboard value and sum with all the values
        sum_list = []
        for drivers_value in drives:
            # for loop till each drives

            # if sum < b:
            if kb_value+drivers_value < b:
                # save it in a list
                sum_list.append(kb_value+drivers_value)
    # save max value from the list into the max_each_list
        if len(sum_list) > 0:
            max_each_with_keyboards.append(max(sum_list))
            # print(max_each_with_keyboards)
    # print(max_each_with_keyboards)
    if len(max_each_with_keyboards) > 0:
        return max(max_each_with_keyboards)
    else:
        return (-1)

    return(keyboards, drives, b)


print(getMoneySet([5, 8, 9], [1, 3], 10))
