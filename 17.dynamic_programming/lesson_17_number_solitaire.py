def solution(A):
    n = len(A)
    current_position = 0
    i = 1
    result = A[0]

    if(n == 0):
        return 0
    if(n == 1):
        return A[1]

    while i < n:
        if i > current_position + 6:
            maxi = A[current_position + 1]
            maxi_index = current_position + 1
            for index in range(current_position + 2, current_position + 7):
                if(A[index] >= maxi):
                    maxi = A[index]
                    maxi_index = index
            result += maxi
            current_position = maxi_index
            i = current_position
        else:
            if(i == n-1):
                result += A[i]
            elif(A[i] > 0):
                result += A[i]
                current_position = i
        i += 1

    return result

#correctness 60% - perf 33% (total 50%) I think I know the issue. I always select the lowest value from the next 6 
#but I don't think that's always correct. Greedy is still on my mind
# inspired by https://stackoverflow.com/questions/34100363/dynamic-programming-codility-q-numbersolitaire

def solution(A):
    n = len(A)
    dices = 6
    max_per_6 = [0] * dices
    max_per_6[dices - 1] = A[0]

    for i in range(1, n):
        maxi = max_per_6[-1] + A[i]
        for dice in range(2, 7):
            if i-dice >= 0:
                maxi = max(maxi, max_per_6[-dice] + A[i])
        max_per_6.append(maxi)
        max_per_6.pop(0)
    return max_per_6[-1]
