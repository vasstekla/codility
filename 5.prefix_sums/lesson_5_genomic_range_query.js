function solution(S, P, Q) {
    let n = S.length
    let m = P.length
    let solution = new Array(m)
    S = S.toString()

    for(let i = 0; i < m; i++) {
        if(S.substring(P[i], Q[i]+1).includes('A')) {
            solution[i] = 1
        } else if(S.substring(P[i], Q[i]+1).includes('C')) {
            solution[i] = 2
        } else if(S.substring(P[i], Q[i]+1).includes('G')) {
            solution[i] = 3
        } else {
            solution[i] = 4
        }
    }
    return solution
}