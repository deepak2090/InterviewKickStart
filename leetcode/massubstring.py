from re import sub


def gcdOfStrings(str1: str, str2: str) -> str:
    substring = ""
    if len(str1) >= len(str2):
        minstring = str2
        maxstring = str1
    else:
        minstring = str1
        maxstring = str2

    result = []
    for k in range(1,len(minstring)+1):
        for i in range(len(minstring)+1):
            if k+i < len(minstring)+1:
                substring = minstring[i:k+i]
                if substring in maxstring:
                    if unique_char(substring):
                        if maxstring[-len(minstring):] == minstring:
                            result.append(substring)
    return result[-1]

def unique_char(string):
    seen_charecters = set()
    for char in string:
        if char in seen_charecters:
            return False
        else:
            seen_charecters.add(char)
    return True

str1 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXX"

result = gcdOfStrings(str1,str2)
print(result)

input = "pwwkew"

def lengthOfLongestSubstring(s: str) -> int:
    dict = {}
    temp = ""
    counter = 0
    i = 0
    tempresult = 0
    if len(s) == 0:
        return 0
    else:
        while i < len(s):
            if s[i] not in dict.keys():
                dict[s[i]] = i
                temp = temp + s[i]
                i+=1
                counter = max(len(temp), tempresult)
            else:
                if len(temp) > tempresult:
                    tempresult = len(temp)
                temp = ""
                i = dict[s[i]] +1
                dict = {}
    return counter

print(lengthOfLongestSubstring("au"))