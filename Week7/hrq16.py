def migratoryBirds(arr):
    # Write your code here
    # sort the array
    # check occurence of each element
    count = {}
    arr.sort()
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    max_key = max(count, key=count.get)
    return(max_key)


migratoryBirds([1, 4, 4, 4, 5, 3])
