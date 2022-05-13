def solution(N):
    if(N == 1):
        return 1

    if(N < 4):
        return 2

    factors = 0

    i = 3
    addition_to_i = 2
    if(N % 2 == 0):
        i = 2
        addition_to_i = 1
    
    while(i*i < N):
        if(N % i == 0):
            factors += 1
        i += addition_to_i
    factors *= 2
    if(N % i == 0 and N / i != i-1):
        factors +=1

    return factors+2