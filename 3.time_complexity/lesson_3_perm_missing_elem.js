function solution(A) {
    if(A.length == 0) {
        return 1
    }
    A = A.sort((a, b) => {return a - b})
    for(let i = 0; i < A.length; i++) {
        if(i + 1 != A[i]) {
            return i + 1
        }
    }
    return A.length + 1
}