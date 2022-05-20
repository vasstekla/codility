def solution(A):
    n = len(A)
    if(n == 1):
        return abs(A[0] + A[0])

    A = sorted(A, key=abs)
    mini = abs(2*max(A))

    for i in range(n - 1):
        mini = min(mini, abs(A[i] + A[i]))
        mini = min(mini, abs(A[i] + A[i + 1]))
        mini = min(mini, abs(A[i + 1] + A[i + 1]))
    return mini
