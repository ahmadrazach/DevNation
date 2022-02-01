def divisibleSumPairs(n, k, ar):
    # Complete this function
    # no. counting variable
    count_paris = 0
    # first loop that goes to the n length
    for i in range(n):
        # second loop that also goes to n
        for j in range(n):
            # if i<j and ar[i]+ar[j]%k==0:
            if i < j and ((ar[i]+ar[j]) % k == 0):
                # count the no.
                count_paris += 1

    # return no. of pairs
    return count_paris


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
