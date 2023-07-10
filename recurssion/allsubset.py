def gcdOfStrings(str1: str, str2: str) -> str:
    substring = ""
    if len(str1) != len(str2):
        minstring = min(str1,str2, key = len)
        maxstring = max(str1,str2, key = len)
    else:
        minstring = str1
        maxstring = str2
    minlen = len(minstring)
    result = []                                                                                                 
    allstring = subset(minstring)
    for xstring in allstring:
            if xstring * (len(maxstring) // len(xstring)) == maxstring:
                result.append(xstring)
                

    return result if len(result) > 0 else ""


def subset(string):
    result = []
    i = 0
    while i < len(string)+1:
        for j in range(len(string)):
            if len(string[j:i]) > 0:
                result.append(string[j:i])
        i +=1
    return sorted(result, key = len)

X = gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")
print(X)

#alternate solution using mathgcd function

import math
def gcdstring(str1, str2):
    if str1 == str2:
        return str1
    if str1+ str2 != str2 + str1:
        return ""
    gcd_len = math.gcd(len(str1), len(str2))
    if str1[:gcd_len] == str2[:gcd_len]:
        return str1[:gcd_len]
    else:
        return ""
print(gcdstring("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))