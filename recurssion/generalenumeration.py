string = "d1epak"

result = []
def helper(s , i , slate):
    if i == len(s):
        result.append(slate)
        return
    if s[i].isdigit():
        helper(s , i +1 , slate + s[i])
    else:
        helper(s, i+1, slate + s[i].swapcase())
        helper(s, i+1, slate + s[i])

def combinations(s):
    slate = ""
    helper(s, 0, slate)
    return result

print(combinations(string), len(result))



def validateparenthesis(parenthesis):
    output = 0
    result = False
    for i in range(len(parenthesis)):
        if output < 0:
            return False
        if parenthesis[i] == '{':
            output +=1
        else:
            output -=1
    if output == 0:
        return True

def helper(s , i , slate):
    if i == len(s):
        if validateparenthesis(slate):
            result.append(slate)
        return
    if s[i].isdigit():
        helper(s , i +1 , slate + s[i])
    else:
        helper(s, i+1, slate + s[i].swapcase())
        helper(s, i+1, slate + s[i])

def combinations(s):
    slate = ""
    helper(s, 0, slate)
    return result

x = "{}{{}}"
print(combinations(x), len(result))

