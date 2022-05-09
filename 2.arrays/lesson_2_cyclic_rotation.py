def solution(A, K):
    A_size = len(A)
    B = A[:]
    if(A_size == K):
        return A
    else:
        for i, element in enumerate(A):
            new_index = (K + i) % A_size
            B[new_index] = element
        return B