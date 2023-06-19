


def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    if a == 1 or b == 0:
        return 1
    elif b == 1:
        return a
    else:
        temp = calculate_power(a , b//2)
        if b % 2 ==0:
            # this is not a good idea to take power of recursion calls better store somewhere
            # return calculate_power(a, b//2) * calculate_power(a, b//2)  % 1000000007
            return temp * temp % 1000000007
        else:
            return temp * temp * a % 1000000007

print(calculate_power(66,7))