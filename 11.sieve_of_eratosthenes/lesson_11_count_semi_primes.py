
def is_semi_prime(N, primes):
    i = 2
    while(i * i <= N):
        if(N % i == 0 and primes[i] == 1 and primes[int(N/i)] == 1):
            return 1
        i += 1
    return 0


def solution(N, P, Q):
    semiprimes_count = [0] * (N + 1)
    semiprimes_count[0] = 0
    semiprimes_count[1] = 0
    primes = [-1] * (N + 1)
    
    i = 2
    while(i < N + 1):
        if(primes[i] == -1):
            primes[i] = 1
            for j in range(i + i, N + 1, i):
                primes[j] = 0
        i += 1
    
    s = len(P)
    result = [0]*s

    for i in range(2, N + 1):
        semiprimes_count[i] = semiprimes_count[i-1] + is_semi_prime(i, primes)

    for i in range(s):
        result[i] = semiprimes_count[Q[i]] - semiprimes_count[P[i] - 1]

    return result

    #100% correct but 40% perf
    #the following is 100% in total

    def solution(N, P, Q):
    semiprimes_count = [0] * (N + 1)
    semiprimes_count[0] = 0
    semiprimes_count[1] = 0
    s_primes = [-1] * (N + 1)
    primes = [-1] * (N + 1)
    
    i = 2
    while(i < N + 1):
        if(primes[i] == -1):
            primes[i] = 1
            for j in range(i + i, N + 1, i):
                primes[j] = 0
        i += 1

    i = 2
    while(i < N + 1):
        if(s_primes[i] == -1):
            s_primes[i] = 0
            for j in range(i + i, N + 1, i):
                s_primes[j] = primes[int(j / i)]
        i += 1

    s = len(P)
    result = [0]*s        

    for i in range(2, N + 1):
        semiprimes_count[i] = semiprimes_count[i-1] + s_primes[i]

    for i in range(s):
        result[i] = semiprimes_count[Q[i]] - semiprimes_count[P[i] - 1]

    return result