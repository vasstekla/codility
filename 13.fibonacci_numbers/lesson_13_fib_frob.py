def solution(A):
    n = len(A)
    fibo = []
    fibo.append(0)
    fibo.append(1)
    calc = 1
    i = 2

    while(calc <= n):
        calc = fibo[i-1] + fibo[i-2]
        fibo.append(calc)
        if(n + 1 == calc):
            return 1
        i += 1

    fibo_len = len(fibo)
    frog_current_position = -1
    count = 0

    while(frog_current_position != n):
        count += 1
        next_jump = 0
        j = fibo_len - 1
        while(next_jump != 1):
            if(j < 0):
                return -1
            next_jump_index = frog_current_position + fibo[j]
            if(next_jump_index == n):
                return count
            if(next_jump_index < n and A[next_jump_index] == 1):
                next_jump = 1
                frog_current_position = next_jump_index
            j -= 1

    return count

#solution 1 with 66% corectness and 16% perf
#solution 2 inspired from https://github.com/OSerHuang/Codility/blob/master/Python/lesson%2013/FibFrog.py 100%

def solution(A):
    A.append(1)
    n = len(A)
    fibo = []
    fibo.append(0)
    fibo.append(1)
    calc = 1
    i = 2

    while(calc <= n):
        calc = fibo[i-1] + fibo[i-2]
        fibo.append(calc)
        if(n == calc ):
            return 1
        i += 1

    dp = {-1: 0}
    for i in range(n):
        if A[i] == 0: continue
        temp_result = []
        for jump in fibo:
            if jump > i + 1: break
            if i - jump in dp:
                temp_result.append(dp[i - jump] + 1)
        if temp_result: dp[i] = min(temp_result)
    return dp.get(n - 1, -1)

