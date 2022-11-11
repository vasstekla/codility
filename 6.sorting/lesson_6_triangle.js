function solution(A) {
    A = A.sort((a, b) => {return a - b}) 
    
    for(let i = 0; i < A.length - 2; i++) {
        let P = A[i]
        let Q = A[i + 1]
        let R = A[i + 2]
        if(P + Q > R && Q + R > P && R + P > Q) {
            return 1
        }
    }

    return 0
}