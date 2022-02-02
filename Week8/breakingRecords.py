scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
#  RETURNS
# int[2]: An array with the numbers of times she broke her records.
# Index 0 return min points records
# Index 1 for breaking max points records.


def breakingRecords(scores):
    min_points = scores[0]
    max_points = scores[0]
    min_count = 0
    max_count = 0
    for i in range(1, len(scores)):
        if scores[i] > max_points:
            max_points = scores[i]
            max_count += 1
        if scores[i] < min_points:
            min_points = scores[i]
            min_count += 1
    return [min_count, max_count]


print(breakingRecords(scores))
