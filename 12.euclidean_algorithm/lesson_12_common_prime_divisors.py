def solution(A, B):
    count = 0
    n = len(A)

    for i in range(n):
        a = A[i]
        b = B[i]

        if(a == b):
            count += 1
        else:
            bigger = A[i]
            smaller = B[i]

            if(bigger < smaller):
                bigger = B[i]
                smaller = A[i]

            if(bigger % smaller == 0):
                if(smaller != 1):
                    while(smaller < (bigger / smaller)):
                        bigger = bigger / smaller
                    if(smaller % (bigger / smaller) == 0):
                        count += 1
    return count

# 85% correctness and 50% perf
# the following code was inspired by https://massivealgorithms.blogspot.com/2015/07/solution-to-common-prime-divisors-by.html

def gcd(x, y):
    if x%y == 0:
        return y
    else:
        return gcd(y, x%y)

def samePrimeDivi(x, y):

    gcd_value = gcd(x, y)

    while x != 1:
        x_gcd = gcd(x, gcd_value)
        if x_gcd == 1:
            break
        x /= x_gcd

    if x != 1:
        return False


    while y != 1:
        y_gcd = gcd(y, gcd_value)
        if y_gcd == 1:
            break
        y /= y_gcd

    return y == 1

def solution(A, B):
    n = len(A)
    count = 0

    for i in range(n):
        if samePrimeDivi(A[i], B[i]):
            count += 1

    return count
