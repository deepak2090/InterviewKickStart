parenthesis = "abcd"
def generate_all_subsets(s):
    result = ['']
    for j in range(len(s)):
        for i in range(len(result)):
            result.append(result[i] + s[j])
    return result
print(generate_all_subsets(parenthesis))