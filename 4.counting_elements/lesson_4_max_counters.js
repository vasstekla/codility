function solution(N, A) {
    let counter = new Array(N).fill(0)
    let minValue = 0
    let maxValue = 0

    for(let i = 0; i < A.length; i++) {
        if(A[i] == N + 1) {
            minValue = maxValue
        } else {
            if(counter[A[i] - 1] < minValue) {
                counter[A[i] - 1] = minValue
            }
            counter[A[i] - 1] += 1
            if(counter[A[i] - 1] > maxValue) {
                maxValue = counter[A[i] - 1]
            }
        }
    }
    
    for(let i = 0; i < counter.length; i++) {
        if(counter[i] < minValue) {
            counter[i] = minValue
        }
    }

    return counter
}