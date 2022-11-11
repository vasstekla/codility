def solution(A):
    B = A[:]
    n = len(A)
    index = 0

    if(n == 0):
        return -1
    
    if(n == 1):
        return 0

    while(n != 1 and index < n-1):
        if(A[index] != A[index+1]):
            A.pop(index)
            A.pop(index)
            n = len(A)
        else:
            index += 1

    if(n == 0):
        return -1

    dominator_candidate = A[n-1]
    dominator_candidate_count = 0
    dominator_candidate_index = 0
    
    for index, elem in enumerate(B):
        if(elem == dominator_candidate):
            dominator_candidate_count += 1
            dominator_candidate_index = index

    if(len(B)/2 < dominator_candidate_count):
        return dominator_candidate_index

    return -1

    #first try - 83% because of the performance **facepalm**. I think the pop is too expensive.
    #yep I was right. Should've gone with my gut from the first second xD 

    def solution(A):
    B = A[:]
    n = len(A)
    index = 0

    if(n == 0):
        return -1
    
    if(n == 1):
        return 0

    A.sort()
    dominator_candidate = A[int(n/2)]
    dominator_candidate_count = 0
    dominator_candidate_index = 0

    for index, elem in enumerate(B):
        if(elem == dominator_candidate):
            dominator_candidate_count += 1
            dominator_candidate_index = index

    if(len(B)/2 < dominator_candidate_count):
        return dominator_candidate_index


    return -1