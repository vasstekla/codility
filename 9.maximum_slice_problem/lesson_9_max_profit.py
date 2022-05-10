def solution(A):
    n = len(A)

    if(n == 0):
        return 0

    #check if the array is sorted already
    B = A[:]
    C = A[:]

    B.sort()
    C.sort(reverse=True)

    ascending = True
    descending = True
    indx = 0

    while(indx < n and (ascending == True or descending == True)):
        if(A[indx] != B[indx]):
            ascending = False
        if(A[indx] != C[indx]):
            descending = False
        indx += 1
    
    if(ascending == True):
        return A[n-1]-A[0]
    if(descending == True):
        return 0

    #if not already sorted
    maxi = max(A) 
    mini = min(A)
    max_value = 0    

    for index in range(n):
        if(A[index] == maxi):
            if(index + 1 < n-1):
                maxi = max(A[index+1:n])
                index += 1
        else:
            max_value = max(maxi - A[index], max_value)
            #if we found the smallest value from the array there is no use in looking anymore
            if(A[index] == mini):
                break
    
    return max_value