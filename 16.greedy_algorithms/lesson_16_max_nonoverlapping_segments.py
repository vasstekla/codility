def solution(A, B):
    n = len(A)
    count = 1
    j = 1

    if(n == 0):
        return 0

    for index in range(n - 1):
        i = index
        j = 0
        current_count = 1
        while(j < n):
            if(B[i] >= A[j]):
                #intersect
                j += 1
            else:
                #not intersect
                current_count += 1
                i = j
                j += 1
        count = max(count, current_count)
                
    return count

# 100% correctness and 20% perf
# 100% correctness and 100% perf - just remove the for cycle

def solution(A, B):
    n = len(A)
    count = 1
    j = 1

    if(n == 0):
        return 0

    i = 0
    j = 0
    current_count = 1
    while(j < n):
        if(B[i] >= A[j]):
            #intersect
            j += 1
        else:
            #not intersect
            current_count += 1
            i = j
            j += 1
    count = max(count, current_count)
                
    return count