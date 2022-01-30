def bonAppetit(bill, k, b):
    total = 0
    for i in range(len(bill)):
        if i != k:
            total += bill[i]
    if total//2 == b:
        print("Bon Appetit")
    else:
        print(b-total//2)
