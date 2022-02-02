s = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1,
     4, 1, 3, 3, 4, 2, 1]  # [1, 2, 1, 3, 2]
d = 18  # 3  # 18
m = 7  # 7
# Returns
# int: the number of ways the bar can be divided


def birthday(s, d, m):
    # your code
    # add_square_values=0
    # contiguous_result=0

    contiguous_result = 0
    prev_result = 0
    # loop to the s
    for i in range(len(s)):
        # loop till m
        add_square_values = 0
        count = 0
        for j in range(i, i+m):
            # add_sqaure_values+=s[j]
            if count == m or j > i:
                print("M's taken")
                break
            else:
                print(" j's index :", j, " value : ", s[j])
                add_square_values += s[j]
                count += 1
        print("Square's value : ", add_square_values)
        # check if add_sqaure values == d:
        if add_square_values == d:
            # check if i==0:
            if i == 0:
                # contiguous_result+=1
                prev_result += add_square_values
                contiguous_result += 1
               # print("prev result : ", prev_result)
            # check if contiguous_result==add_square values
            elif prev_result == add_square_values:
                prev_result += add_square_values
                contiguous_result += 1
            else:
                pass
        else:
            pass
        #print("Contigeofj values : ", contiguous_result)
    return(int(contiguous_result))


print(birthday(s, d, m))
