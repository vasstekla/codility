function solution(A) {
    let map = new Map()

    for(let i = 0; i < A.length; i++) {
        map.set(A[i], 1)
    }
    for(let i = 1; i <= A.length; i++) {
        if(!map.has(i)) {
            return 0
        }
    }
    return 1
}