def sockMerchant(n, ar):
    ar.sort()  # sort the array
    count = 0
    # loop through the array and check if the next element is the same as the current element
    for i in range(len(ar)-1):
        # if the next element is the same as the current element
        if ar[i] == ar[i+1]:
            count += 1
            ar[i] = 0  # set the current element to 0
            ar[i+1] = 0  # set the next element to 0
    return count  # return the count
