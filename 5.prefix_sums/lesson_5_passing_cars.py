def solution(A):
    n = len(A)
    if n == 1:
        return 0

    #reverse list
    A = A[::-1]
    
    prefix_sums = [0] * n
    prefix_sums[0] = A[0]

    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + A[i]

    count = 0
    for index, elem in enumerate(A):
        if(elem == 0):
            count += prefix_sums[index]
        
    if(count <= 1000000000):
        return count

    return -1