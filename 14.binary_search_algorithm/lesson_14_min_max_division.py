def solution(K, M, A):
    n = len(A)
    prefixes = [0]*n
    prefixes[0] = A[0]

    for i in range(1,n):
        prefixes[i] = prefixes[i-1] + A[i]
    
    begin = max(A)
    end = prefixes[n-1]
    result = 0

    while(begin <= end):
        mid = int((begin+end)/2)
        curr_sum = 0
        blocks = 1

        for i in range(n):
            if(curr_sum + A[i] > mid):
                blocks += 1
                curr_sum = A[i]

                if(blocks > K):
                    break
            else:
                curr_sum += A[i]
        
        if blocks > K:
            begin = mid + 1
        else:
            result = mid
            end = mid - 1

    return result