def solution(A):
    all_sum = 0
    max_value = 0
    current_half_sum = 0
    for i in A:
        all_sum += i
        max_value += abs(i)
    min_value = max_value
    for index in range(len(A)-1):
        current_half_sum += A[index]
        difference = abs(2*current_half_sum - all_sum)
        if(difference < min_value):
            min_value = difference
    return min_value