def solution(A):
    n = len(A)
    if(n < 3):
        return 0
    A.sort()
    result = 0
    P = 0
    Q = 1
    R = 2

    while(P < n and Q < n and R < n):
        if(A[P] + A[Q] <= A[R]):
                Q += 1
                R = Q
        else:
            if(A[P] + A[Q] > A[R] and A[P] + A[R] > A[Q] and A[R] + A[Q] > A[P]):
                result += 1
            
           
        R += 1
        if(R >= n):
            if(Q + 1 <= n - 2):
                Q += 1
                R = Q + 1
            else:
                if(P + 1 <= n - 3):
                    P += 1
                    Q = P + 1
                    R = Q + 1
        
    return result

# 100% solution 0% perf - total 63%
# the following was inspired by https://github.com/porsk/codility/blob/main/15-caterpillar-method/countTriangles.js

def solution(A):
    n = len(A)
    if(n < 3):
        return 0
    A.sort()
    result = 0

    for P in range(n - 2):
        Q = P + 1
        R = P + 2

        while(Q < n - 1):
            if(R < n and A[P] + A[Q] > A[R]):
                R += 1
            else:
                Q += 1
                result += R - Q
        
    return result
