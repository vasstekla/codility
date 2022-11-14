function solution(A) {
    let maxSum = A[0]
    let maxSumEnd = A[0]

    for(let i = 1; i < A.length; i++) {
        maxSumEnd = Math.max(A[i], maxSumEnd + A[i])
        maxSum = Math.max(maxSum, maxSumEnd)
    }

    return maxSum
}