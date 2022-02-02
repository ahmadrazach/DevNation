# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p

def pageCount(n, p):
    # complete this function
    # page_turns=1
    page_turns_front = 0
    # page_side=0
    page_side = 0
    # checking from front
    # loop till the n
    for i in range(n):
        # check if pages are two
        if page_side == 2:
            page_turns_front += 1

            page_side = 0
        # page_turns_front+=1
            # page_side=0
        # check if i==p:
        if i == p:
            #   break
            break
        # else:
        else:
            # page_side+=1
            page_side += 1
    # checking from back
    page_side = 0
    page_turns_back = 0
    for i in range(n, 1, -1):
        # check if pages are two
        if page_side == 2 or i == n:
            page_turns_back += 1

            page_side = 0
        # page_turns_front+=1
            # page_side=0
        # check if i==p:
        if i == p:
            #   break
            break
        # else:
        else:
            # page_side+=1
            page_side += 1
        print("i : ", i)
    print("Page Turns : front ", page_turns_front, " back : ", page_turns_back)
    return(min(page_turns_front, page_turns_back))


print(pageCount(6, 5))
