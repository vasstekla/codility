def solution(A):
    maxi = 0
    for element in A:
        if(maxi < element):
            maxi = element
    if(maxi != len(A)):
        return 0
    occurs = [False] * maxi
    for element in A:
        occurs[element-1] = True
    if(False in occurs):
        return 0
    return 1