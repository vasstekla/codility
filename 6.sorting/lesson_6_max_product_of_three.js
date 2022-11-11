function solution(A) {
    let negative = new Array()
    let positive = new Array()
    let maximum = Number.MIN_SAFE_INTEGER

    if(A.length == 3) {
        return A[0] * A[1] * A[2]
    }

    for(let i = 0; i < A.length; i++) {
        if(A[i] < 0) {
            negative.push(A[i])
        } else {
            positive.push(A[i])
        }
    }

    negative = negative.sort((a, b) => {return a - b})
    positive = positive.sort((a, b) => {return b - a})

    let n = negative.length
    let p = positive.length
    let curr = 0

    if(p == 0) {
        return negative[n - 1] * negative[n - 2] * negative[n - 3]
    }

    if(n == 0) {
        return positive[0] * positive[1] * positive[2]
    }

    if(n > 1 && p != 0) {
        curr = negative[0] * negative[1] * positive[0]
        if(curr > maximum) {
            maximum = curr
        }
    }

    if(p > 2) {
        curr = positive[0] * positive[1] * positive[2]
        if(curr > maximum) {
            maximum = curr
        }
    }

    return maximum
}