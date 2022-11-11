function solution(A) {
    let n = A.length
    let map = new Map()
    let count = 0
    let firstSequence = new Map()
    let secondSequence = map
    let leader = 0
    let leaderOcc = 0

    if(n == 0 || n == 1) {
        return 0
    }

    for(let i = 0; i < n; i++) {
        let elem = A[i]
        if(map.has(elem)) {
            map.set(elem,  map.get(elem) + 1)
        } else {
            map.set(elem, 1)
        }
    }

    for(let i = 0; i < n; i++) {
        let a = A[i]
        if(firstSequence.has(a)) {
            let leaderCount = firstSequence.get(a) + 1
            firstSequence.set(a, leaderCount)
            if(leaderCount > leaderOcc) {
                leaderOcc = leaderCount
                leader = a
            }
        } else {
            firstSequence.set(a,1)
            if(leader == 0) {
                leader = a
            }
        }
        secondSequence.set(a, secondSequence.get(a) - 1)

        if(firstSequence.has(leader) && firstSequence.get(leader) > (i+1) / 2 && secondSequence.get(leader) > (n - i - 1) / 2) {
            count ++
        }
    }

    return count
}