def solution(A):
    s = len(A)

    if(s == 2):
        return 0

    prefixes = [0]*s
    prefixes[0] = A[0]

    for index in range(1, s):
        prefixes[index] = prefixes[index-1] + A[index]

    min_value = 11000
    min_index = -1

    for i in range(s-1):
        maxi = i+3
        if(maxi > s):
            maxi = s
        for j in range(i+1, maxi):
            summ = prefixes[j] 
            if(i > 0):
                summ -= prefixes[i-1]
            current_avg = summ / (j - i + 1)
            if(current_avg < min_value):
                min_value = current_avg
                min_index = i
    return min_index