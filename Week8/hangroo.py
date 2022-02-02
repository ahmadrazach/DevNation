def kangaroo(x1, v1, x2, v2):
    # Write your code here
    x1_kangroo = x1+v1
    x2_kangroo = x2+v2
    count = 0
    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        while(x1_kangroo <= 100000000 and x2_kangroo <= 100000000):
            count += 1
            # a loop untill x1 <=1000
            if x1_kangroo == x2_kangroo:
                print("x1 : ", x1_kangroo)
                print("x2 : ", x2_kangroo)
                print("count : ", count)
                return "YES"
            else:
                x1_kangroo += v1
                x2_kangroo += v2
        print("x1 : ", x1_kangroo)
        print("x2 : ", x2_kangroo)
        return "NO"


print(kangaroo(2081, 8403, 9107, 8400))
