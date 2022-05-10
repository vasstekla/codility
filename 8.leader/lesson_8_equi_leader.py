def solution(A):
    B = A[:]
    n = len(A)
    
    if(n == 2 and A[0] == A[1]):
        return 1

    if(n < 3):
        return 0

    A.sort()

    leader_candidate = A[int(n/2)]
    leader_candidate_count = 0

    for elem in A:
        if(elem == leader_candidate):
            leader_candidate_count += 1
    
    if(n/2 >= leader_candidate_count):
        return 0

    for index in range(n):
        if(B[index] == leader_candidate):
            B[index] = 1
        else:
            B[index] = -1

    prefix_sums = [0]*n
    prefix_sums[0] = B[0]

    for index in range(1, n):
        prefix_sums[index] = prefix_sums[index - 1] + B[index]

    equi_leader_count = 0
    for index in range(n-1):
        if(prefix_sums[index] > 0 and prefix_sums[n-1]-prefix_sums[index] > 0):
            equi_leader_count += 1

    return equi_leader_count