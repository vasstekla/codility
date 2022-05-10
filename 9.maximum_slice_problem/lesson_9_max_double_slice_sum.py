def solution(A):
    n = len(A)

    if(n < 4):
        return 0
    prefix_sums = [0]*n
    prefix_sums[0] = A[0]

    for index in range(1,n):
        prefix_sums[index] = prefix_sums[index-1] + A[index]

    max_slice_sum = min(A)
    start_index = 0


    for i in range(3, n):
        if(i != start_index+1):
            y = min(A[start_index+1:i])
            pref = prefix_sums[i-1] - prefix_sums[start_index] - y
            if(pref < A[i-1]):
                start_index = i
                max_slice_sum = max(max_slice_sum, A[i-1])
            else:
                max_slice_sum = max(max_slice_sum, pref)

    return max_slice_sum

    #I tried to adapt the max_slice_sum problem, however it gives 0% performance (100% correctness, which is weird 
    #because the perf tests don't give correct answers)
    #the following solution was inspired by https://medium.com/@deck451/codility-algorithm-practice-lesson-9-maximum-slice-problem-task-3-maxdoubleslicesum-a-python-662b74bf4b3e
    #mmm okkaaayyy

    def solution(A):
        max_slice_sum = 0
        n = len(A)
        fwd = [0] * n
        bkw = [0] * n

        for i in range(1, n - 1):
            fwd[i] = max(fwd[i - 1] + A[i], 0)

        for i in range(n - 2, 0, -1):
            bkw[i] = max(bkw[i + 1] + A[i], 0)
        
        for i in range(1, n - 1):
            max_slice_sum = max(max_slice_sum, fwd[i - 1] + bkw[i + 1])
        return max_slice_sum