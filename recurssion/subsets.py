#iterative
parenthesis = "abcd"
def generate_all_subsets(s):
    result = []
    for j in range(len(s)):
        for i in range(len(result)):
            result.append(result[i] + s[j])
    return result
print(generate_all_subsets(parenthesis))

#recusrsion code for generating subsets

parenthesis = "abcd"

def generate_subset_recurssion(s):
    result = ['']
    helper(s, 0 , result)
    return result

def helper(s, idx , result):
    if idx == len(s):
        return
    for i in range(len(result)):
        result.append(result[i] + s[idx])
    helper(s, idx +1, result)


print(generate_subset_recurssion(parenthesis))

