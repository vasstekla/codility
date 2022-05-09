def solution(A):
    A.sort()
    a = len(A)
    
    if(a == 0):
        return 0
    
    count = 1
    
    for i in range(1, a):
        if(A[i-1] != A[i]):
            count += 1

    return count