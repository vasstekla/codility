def solution(A):
    n = len(A)
    prefix_sums = [0]*n
    prefix_sums[0] = A[0]

    for index in range(1,n):
        prefix_sums[index] = prefix_sums[index-1] + A[index]

    max_slice_sum = A[0]
    start_index = 0

    for i in range(1,n):
        pref = prefix_sums[i]
        if(start_index > 0):
            pref -= prefix_sums[start_index - 1]
        if(pref < A[i]):
            start_index = i
            max_slice_sum = max(max_slice_sum, A[i])
        else:
            max_slice_sum = max(max_slice_sum, pref)

    return max_slice_sum
