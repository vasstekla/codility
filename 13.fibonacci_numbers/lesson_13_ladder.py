def solution(A, B):
    n = len(A)
    maxi = max(A)

    fibo = []
    fibo.append(1)
    fibo.append(1)
    i = 2
    j = 4

    while(i <= maxi):
        fibo.append((fibo[i-1] + fibo[i-2]) % (j))
        i += 1
        j *= 2

    results = [0] * n
    for i in range(n):
        results[i] = int(fibo[A[i]] % (2**B[i]))

    return results

# doesn't give 100% perf because of the modulo so we do bit shift


def solution(A, B):
    n = len(A)
    modLimit = (1 << max(B)) - 1 
    fibo = [1,1]

    for i in range(2, n + 1):
        fibo.append((fibo[i-1] + fibo[i-2]) & modLimit)

    results = [0] * n
    for i in range(n):
        results[i] = int(fibo[A[i]] & ((1<<B[i])-1))

    return results