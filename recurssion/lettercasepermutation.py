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
        
