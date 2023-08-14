


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

def fibonacci(n):
    i = n
    if n == 0 or n ==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonaci_iterative(n):
    if n ==0:
        return [0]
    if n ==1:
        return [0,1]
    else:
        result = [0,1]
        for n in range(2,n):
            result.append(result[-1] +result[-2])
    return result

