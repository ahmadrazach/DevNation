from unicodedata import digit


grades = [63, 67, 38, 33]

for i in range(len(grades)):

    if int(grades[i]) > 37:
        # for saving 2nd digit in the variable
        string = str(grades[i])
        second_digit = int(string[1])
        # checking if number's iltiple of 5 is less than 3
        if (second_digit > 0 and second_digit < 5 and second_digit-3 >= 0):
            grades[i] = 5*round(int(grades[i])/5)

        if(second_digit > 7):
            first_digit = int(string[0])+1
            number = str(int(string[0])+1)+"0"
            grades[i] = int(number)

    print(" Upgraded grades : ", grades[i])
