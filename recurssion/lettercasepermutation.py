s = "a1b2c3"

#immuatable approach

def lettercasepermutation(s):
    result = []
    

    def helperfunction(s, i, slate):
        if i == len(s):
            result.append(slate)
            return
        if s[i].isdigit():
            helperfunction(s, i+1, slate + s[i])
        else:
            helperfunction(s, i+1, slate + s[i].swapcase())
            helperfunction(s, i+1, slate + s[i])
    helperfunction(s,0,"")
    return result

print(lettercasepermutation(s))
print(" all combinations are below")
s1 = "abcde"

def allcombinations(s):
    result = []

    def helperfunction(s, i, slate):
        if i == len(s):
            result.append(slate)
            return
        else:
            for x in range(len(s)):
                if s[x] not in slate:
                    helperfunction(s, i+1, slate + s[x])
            
    helperfunction(s, 0, "")
    return result

print(allcombinations(s1))

#mutable solution


        
