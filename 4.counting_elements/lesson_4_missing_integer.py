def solution(A):
    #if all elements are negative
    all_negative = True
    for elem in A:
        if(elem > 0):
            all_negative = False
            break
    if all_negative:
        return 1
    
    max_number = max(A)
    occurance_is_missing = [True] * max_number

    for elem in A:
        if (elem > 0):
            occurance_is_missing[elem-1] = False

    #return the first missing value
    for i, elem in enumerate(occurance_is_missing):
        if (elem == True):
            return i+1

    #if there is no missing value between 1 and max_number we return the next one
    return max_number + 1
