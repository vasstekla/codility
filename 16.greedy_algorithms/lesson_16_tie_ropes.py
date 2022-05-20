def solution(K, A):
    n = len(A)
    i = 0
    count = 0
    summ = 0

    while(i < n):
        if(A[i] + summ < K):
            summ += A[i]
        else:
            count += 1
            summ = 0
        i += 1

    return count