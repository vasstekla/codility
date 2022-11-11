function solution(A) {
    if(A.length == 0) {
        return 0
    }
    
    A = A.sort((a, b) => {return a - b})
    let distinctCount = 1
    let prevElement = A[0]
    for(let i = 1; i < A.length; i++) {
        if(A[i] != prevElement) {
            distinctCount++
            prevElement = A[i]
        }
    }
    return distinctCount
}
