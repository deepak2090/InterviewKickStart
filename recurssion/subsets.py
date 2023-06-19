parenthesis = "abcd"
def generate_all_subsets(s):
    subset = ['']
    for i in range(len(s)):
        length = len(subset)
        for j in range(length):
            subset.append(subset[j] + s[i])
    return subset

print(generate_all_subsets(parenthesis))

#learn tomorrow