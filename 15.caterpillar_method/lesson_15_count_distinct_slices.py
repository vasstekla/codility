def solution(M, A):
    n = len(A)
    count = 0
    
    for i in range(n):
        k = n
        while(len(set(A[i:k])) != (k - i)):
            k -= 1
        count += k - i
    return count

#perf 0% but correctness 100%
#perf 20% but correctness 100%

def solution(M, A):
    n = len(A)
    if(n == 1):
        return 1
    occurance = [0] * (M + 1)
    for elem in A:
        occurance[elem] += 1
    count = 0
    
    for i in range(n):
        curr_count = 0
        curr_occurance = occurance [:]
        for j in range(i, n):
            curr_occurance[A[j]] -= 1
            if(occurance[A[j]] - 2 == curr_occurance[A[j]]):
                break
            curr_count += 1
        count += curr_count      

    return count

#inspired by https://github.com/porsk/codility/blob/main/15-caterpillar-method/countDistinctSlices.js the following solution is 100%
#note: I tried using list but it is necessarry to use sets because of the performance (with lists you'll get a total of 70%)

def solution(M, A):
    n = len(A)
    
    left = right = 0
    elements = set()
    result = n

    while(left < n and right < n):
        if(A[right] in elements):
            elements.remove(A[left])
            left += 1
        else:
            result += right - left
            elements.add(A[right])
            right += 1

        if result > 1000000000:
            return 1000000000

    return result