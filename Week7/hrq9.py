candles = [3, 2, 1, 3]
count_candles = []
for i in range(len(candles)):
    for j in range(i+1, len(candles), 1):
        if int(candles[j]) == int(candles[i]):
            count_candles.append(1)
            max_num = int(candles[i])
            print("i's :", i, "j :", j, " ", candles[i])
        else:
            count_candles.append(0)

print(max_num)
print(count_candles)
print(max(count_candles)+1)
