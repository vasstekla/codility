function solution(A, K) {
    let a = A.length
    let rotate = K % a
    let rotatedA = new Array(a)

    for(let i = 0; i < a; i++) {
        let j = i + rotate
        if(j >= a) {
            j -= a
        }
        rotatedA[j] = A[i]
    }
    return rotatedA
}