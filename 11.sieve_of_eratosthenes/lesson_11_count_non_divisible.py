def solution(A):
    n = len(A)
    B = A[:]
    C = dict.fromkeys(A, 0)

    if(n == 1):
        return [0]

    B.sort()
    prev = -1

    for i in range(n-1, -1, -1):
        if(prev != B[i]):
            prev = B[i]
            count = n-1-i

            for j in range(i-1, -1, -1):
                if(B[i] % B[j] != 0):
                    count += 1
            C[B[i]] = count
    
    result = [0]*n
    for i in range(n):
        result[i] = C[A[i]]
        
    return result

#solution 100%, perf25% 
#the following is 100% but it killed my mental health. one test died constantly ... then I made count to be +1 and 
#thus count[A[index]] instead of count[A[index]-1] and that worked o.O (obv replacing it also everywhere) fml

def solution(A):
    n = len(A)
    count = [0]*(2*n+1)

    if(n == 1):
        return [0]

    for index in range(n):
        count[A[index]] += 1

    result = [0]*n
    C = dict.fromkeys(A, -1)

    for i in range(n):
        j = 2
        res = 0
        a = A[i]
        if(C[a] == -1):
            if(a == 1):
                C[a] = n - count[1]
            else:
                while(j * j <= a):
                    if(a % j == 0):
                        res += count[j]
                        if(a /j != j):
                            res += count[int(a/j)]
                    j += 1
                C[a] = n - res - count[1] - count[a]
        result[i] = C[a]

    return result

