def solution(X, A):
    if(len(A) == 1):
        if(A[0] == 1):
            return 0
        else:
            return -1

    first_occurance = [-1] * X
    for time, position in enumerate(A):
        if(first_occurance[position - 1] == -1):
            first_occurance[position - 1] = time
    maxi = 0
    for occurance in first_occurance:
        if(occurance == -1):
            return -1
        if(occurance > maxi):
            maxi = occurance
    return maxi