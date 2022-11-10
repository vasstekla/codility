function solution(A) {
    let n = A.length
    let pairs = 0
    let prefSums = new Array(n)
    prefSums[0] = A[0]
    
    for(let i = 1; i < n; i++) {
        prefSums[i] = prefSums[i-1] + A[i]
    }

    for(let i = 0; i < n; i++) {
        if(A[i] == 0) {
            pairs += (prefSums[n-1] - prefSums[i])
        }
    }

    if(pairs > 1000000000) {
        return -1
    }
    
    return pairs
}