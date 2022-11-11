function solution(A) {
    let map = new Map()
    let max = 1
    let index = -1

    if(A.length == 0) {
        return -1
    }

    if(A.length == 1) {
        return 0
    }

    for(let i = 0; i < A.length; i++) {
        let elem = A[i]
        if(map.has(elem)) {
            let occ = map.get(elem) + 1
            map.set(elem, occ)
            if(occ > max) {
                max = occ
                index = i
            }
        } else {
            map.set(elem, 1)
        }
    }

    if(max > A.length / 2) {
        return index
    }

    return -1
}