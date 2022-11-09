function solution(X, A) {
    let map = new Map()
    for(let i = 1; i <= X; i++) {
        map.set(i, 1)
    }

    for(let i = 0; i < A.length; i++) {
        if(map.has(A[i])) {
            map.delete(A[i])
        }
        if(map.size == 0) {
            return i
        }
    }
    return -1
}