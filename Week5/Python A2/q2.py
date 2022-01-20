input1 = input("Enter true or false : ")
input2 = input("Enter True or False : ")
xor_result = bool(False)
if(input1 == "True"):
    input1 = bool(True)
else:
    input1 = bool(False)
if(input2 == "True"):
    input2 = bool(True)
else:
    input2 = bool(False)

if(input1 != input2):
    xor_result = True
print("XOR Result : ", xor_result)
