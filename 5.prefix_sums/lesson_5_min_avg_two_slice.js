function solution(A) {
    let n = A.length
    let min = 10000 * n
    let minIndex = 0

    for(let i = 0; i < n - 1; i++) {
        let sum = A[i]
        let end = i + 4 > n ? n : i + 4
        for(let j = i + 1; j < end; j++) {
            sum += A[j]
            let div = sum / (j - i + 1)
            if(div < min) {
                min = div
                minIndex = i
            }
        }
    }
    return minIndex
}