function solution(A) {
    let discPairs = 0
    for(let i = 0; i < A.length - 1; i++) {
        let start = i - A[i]
        let end = i + A[i]
        for(let j = i + 1; j < A.length; j++) {
            let startj = j - A[j]
            let endj = j + A[j]
            if(end >= startj && start <= endj) {
                discPairs++
            }
        }
    }

    if (discPairs > 10000000) {
        return - 1
    }

    return discPairs
}

// first solution was not quite 100% on the performance
// second is 100% using a stack

function solution(A) {
    let edgePoints = Array.from(Array(2*A.length), () => new Array(2));
    let openDiscs = new Array()
    let discPairs = 0
    let j = 0

    for(let i = 0; i < A.length; i++) {
        edgePoints[j][0] = 0 // start point
        edgePoints[j][1] = i - A[i]
        edgePoints[j + 1][0] = 1 // end point
        edgePoints[j + 1][1] = i + A[i]
        j += 2
    }

    edgePoints = edgePoints.sort((a, b) => {return a[1] - b[1]})
    edgePoints = edgePoints.sort((a, b) => {
        if(a[1] == b[1] && a[0] == 0) {
            return -1
        }
    })
    
    for(let i = 0; i < edgePoints.length; i++) {
        if(edgePoints[i][0] == 0) {
            if(openDiscs.length != 0) {
                discPairs += openDiscs.length
            }
            openDiscs.push(edgePoints[i][0])
        } else {
            openDiscs.pop()
        }
    }

    if (discPairs > 10000000) {
        return - 1
    }

    return discPairs
}
