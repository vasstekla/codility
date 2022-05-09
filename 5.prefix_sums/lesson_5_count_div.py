def solution(A, B, K):
    first_number = A
    while(first_number % K != 0):
        first_number += 1
    
    count = 0
    while(first_number <= B):
        first_number += K
        count += 1

    return count

#this was my first try, which was correct, however it wasn't passing the performance
#then my bf told me that there is a solution with O(1)
#so my second try was this, which is 100%

def solution(A, B, K):
    result = int(B / K) - int(A / K)
    if(A % K == 0):
        return result + 1
    return result