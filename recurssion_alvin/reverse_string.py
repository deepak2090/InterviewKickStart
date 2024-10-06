from math import remainder


def reverse_string(string_input):
    if string_input == "":
        return ""
    elif len(string_input) ==1:
        return string_input
    else:
        return string_input[-1] + reverse_string(string_input[:-1])

def pallindromecheck(stringinput):
    if len(stringinput) ==1 or len(stringinput) ==0:
        return True
    if stringinput[0] == stringinput[-1]:
        return pallindromecheck(stringinput[1:-1])
    return False
print(pallindromecheck("deepak"))
print(pallindromecheck("kayak"))

def decimaltobinary(value):
    def helperfunc(value, slate):
        if value ==1 or value==0:
            slate.append(value)
            return slate[:]
        newvalue = value//2
        remainder = value %2
        slate.append(remainder)
        #print(slate[:])
        return helperfunc(newvalue, slate[:])
    x = helperfunc(value, [])
    charecter = ""
    for char in x:
        charecter +=str(char)
    return charecter[::-1]

print(decimaltobinary(5))


