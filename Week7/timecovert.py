def timeConversion(s):
    # Complete this function

    if s[-2:] == "PM":  # if PM
        if s[:2] == "12":
            print(s[:-2])
        else:
            print(str(int(s[:2])+12)+s[2:-2])
    elif s[-2:00] and s[:2] == "12":
        print("00"+s[2:-2])
    elif s[-2:] == "AM" and s[:2] == "12":
        print("00" + s[2:-2])
    elif s[-2:] == "AM":  # 1AM -> 01:00
        print(s[:-2])
    elif s[-2:] == "PM" and s[:2] == "12":  # 12PM -> 12:00
        print(s[:-2])
    else:  # 1PM -> 13:00
        print(str(int(s[:2])+12)+s[2:-2])


timeConversion("12:40:22AM")
