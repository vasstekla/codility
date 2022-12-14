function solution(N, P, Q) {
    if (N == 1) {
        return [0]
    }

    let n = N
    let m = P.length

    let primes = new Array(n + 1).fill(true)
    let onlyPrimes = new Array()
    let semiprimes = new Array(N + 1).fill(0)
    let prefixSum = new Array(N + 1)
    let result = new Array(m)

    primes[0] = false
    primes[1] = false

    for (let i = 2; i * i < n; i++) {
        for (let j = i + i; j < n; j += i) {
            primes[j] = false
        }
    }

    for (let i = 2; i < n + 1; i++) {
        if (primes[i]) {
            onlyPrimes.push(i)
        }
    }

    for (let i = 0; i < onlyPrimes.length; i++) {
        for (let j = i; j < onlyPrimes.length; j++) {
            let product = onlyPrimes[i] * onlyPrimes[j]
            if (product < N + 1) {
                semiprimes[product] = 1
            }
        }
    }
    prefixSum[0] = semiprimes[0]

    for (let i = 1; i < N + 1; i++) {
        prefixSum[i] = prefixSum[i - 1] + semiprimes[i]
    }


    for (let i = 0; i < m; i++) {
        result[i] = prefixSum[Q[i]] - prefixSum[P[i] - 1]
    }

    return result
}