
num ="51230000"
def removeTrailingZeros(num: str) -> str:
    while num[-1] =="0":
        num = num.removesuffix(num[-1])
    return num


print(removeTrailingZeros(num))