total_classes = input("No. of classes held :")
taken_classes = input("Taken classes :")
total_classes = float(total_classes)
taken_classes = float(taken_classes)
percentage = int((taken_classes/total_classes)*100)
if total_classes < taken_classes or percentage > 100 or percentage < 0:
    print("Wrong input given")
elif percentage >= 75:
    print("You can give exam")
elif percentage < 75:
    print("Not allowed")
