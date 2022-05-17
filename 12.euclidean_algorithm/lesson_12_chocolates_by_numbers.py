#v.1. 100% correctness, 0% performance
def solution(N, M):
    X = 0
    chocolates_eaten = 1
    chocolates = [0]*N
    chocolates[0] = 1
    calc = int((X+M)%N)

    while(chocolates[calc] != 1):
        X = calc
        chocolates_eaten += 1
        chocolates[calc] = 1
        calc = int((X+M)%N)

    return chocolates_eaten

#v.2. 100% correctness, 25% performance
def solution(N, M):
    X = 0
    chocolates_eaten = 1
    calc = int((X+M)%N)

    while(calc != 0):
        X = calc
        chocolates_eaten += 1
        calc = int((X+M)%N)

    return chocolates_eaten

#v.3. 100% on both

def gcdByDivision(N, M):
    if(N % M == 0):
        return M
    return gcdByDivision(M, N % M)

def solution(N, M):
    return int(N / gcdByDivision(N, M))

