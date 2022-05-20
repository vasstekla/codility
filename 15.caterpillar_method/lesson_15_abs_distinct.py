
def solution(A):
    n = len(A)
    begin = 0
    end = n - 1
    count = 1

    while(begin != end and begin < end):
        if(abs(A[begin]) == abs(A[end])):
            if(begin + 1 != end):
                if( abs(A[end]) != abs(A[end - 1]) and begin != end - 1):
                    count += 1
                elif( abs(A[begin]) != abs(A[begin + 1]) and end != begin + 1):
                    count += 1
            end -= 1
            begin += 1
        elif(abs(A[begin]) < abs(A[end])):
            if(abs(A[end]) != abs(A[end - 1])):
                count += 1
            end -= 1
        elif(abs(A[begin]) > abs(A[end])):
            if( abs(A[begin]) != abs(A[begin + 1])):
                count += 1
            begin += 1

    return count

#tried with the caterpillar method but got really lost in it
#so I hacked through it - 100% O(N) or O(N*log(N))

def solution(A):
    return len(list(set(abs(a) for a in A)))