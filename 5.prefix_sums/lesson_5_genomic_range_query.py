def solution(S, P, Q):
    nucleotides = { 'A': 1, 'C': 2, 'G': 3, 'T': 4 }
    p = len(P)
    result = [0] * p
    

    for index in range(p):
        if(P[index] == Q[index]):
            result[index] = nucleotides[S[P[index]]]
        else:
            if('A' in S[P[index]:Q[index]+1]):
                result[index] = 1
            elif('C' in S[P[index]:Q[index]+1]):
                result[index] = 2
            elif('G' in S[P[index]:Q[index]+1]):
                result[index] = 3
            else:
                result[index] = 4
    return result