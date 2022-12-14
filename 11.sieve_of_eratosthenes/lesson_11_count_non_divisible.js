function solution(A) {
    let n = A.length
    let max = Math.max(...A)
    let occurance = new Array(max + 1).fill(0)
    let divisors = new Array(max + 1).fill(0)
    let result = new Array(n).fill(0)

    for (let i = 0; i < n; i++) {
        occurance[A[i]] += 1
    }

    for (let i = 1; i <= max; i++) {
        divisors[i] += occurance[i]
        for (let j = i + i; j <= max; j += i) {
            divisors[j] += occurance[i]
        }
    }

    for (let i = 0; i < n; i++) {
        result[i] = n - divisors[A[i]]
    }

    return result
}