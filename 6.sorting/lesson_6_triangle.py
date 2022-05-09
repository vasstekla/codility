def solution(A):
    s = len(A)
    A.sort()

    if(s < 3):
        return 0

    for index in range(s-2):
        if(A[index+2] - A[index] < A[index+1]):
            return 1

    return 0