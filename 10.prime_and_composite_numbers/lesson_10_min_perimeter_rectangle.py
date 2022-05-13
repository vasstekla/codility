def solution(N):
    sqrt = int(N**(1/2))
    mini = 2 * (1 + N)
    for i in range(sqrt, 1, -1):
        if(N % i == 0):
            mini = min(mini, 2 * (i + int(N / i)))
    return mini