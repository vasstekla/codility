def solution(A):
    s = len(A)
    triplet = 1
    if(s < 4):
        for a in A:
            triplet *= a
        return triplet

    A.sort()

    #if the whole array is positive or negative
    if(A[0] > 0 or A[s-1] < 0):
        return A[s-1]*A[s-2]*A[s-3]

    #if mixed - positive and negative values divide into two
    for index, elem in enumerate(A):
        if(elem >= 0):
            biggest_two_neg_one_pos = A[s-1]*A[0]*A[1]
            biggest_three_pos = A[s-1]*A[s-2]*A[s-3]
            return max([biggest_two_neg_one_pos, biggest_three_pos])