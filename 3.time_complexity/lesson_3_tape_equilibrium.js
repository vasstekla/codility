function solution(A) {
    let a = A.length
    let result = 100000
    let prefix_sum = new Array(a).fill(0)
    prefix_sum[0] = A[0]
    for(let i = 1; i < a; i++) {
        prefix_sum[i] = prefix_sum[i-1] + A[i]
    }

    for(let i = 0; i < a; i++) {
        if(i != a-1) {
        let abs = Math.abs(prefix_sum[i] - (prefix_sum[a-1]-prefix_sum[i]))
                if (abs < result) {
                    result = abs
                }
        }
    }
    return result
}