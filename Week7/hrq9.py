candles = [3, 2, 1, 3]
counter = 0
num = candles[0]
for i in range(len(candles)):
    if(candles[i] > num):
        num = candles[i]
for i in range(len(candles)):
    if candles[i] == num:
        counter += 1

print(counter)
