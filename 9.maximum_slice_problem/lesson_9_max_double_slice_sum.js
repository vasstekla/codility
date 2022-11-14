function solution(A) {
    if(A.length == 3) {
        return 0
    }

    let maxSumToN = new Array(A.length).fill(0)
    let maxSumTo0 = new Array(A.length).fill(0)
    let max = 0

    for(let i = 1; i < A.length - 1; i++) {
        maxSumToN[i] = Math.max(maxSumToN[i - 1] + A[i], 0)
    }
    for(let i = A.length - 2; i >= 0; i--) {
        maxSumTo0[i] = Math.max(maxSumTo0[i + 1] + A[i], 0)
    }
    for(let i = 1; i < A.length - 1; i++) {
        max = Math.max(max, maxSumToN[i - 1] + maxSumTo0[i + 1])
    }

    return max
}

//inspired from https://medium.com/@deck451/codility-algorithm-practice-lesson-9-maximum-slice-problem-task-3-maxdoubleslicesum-a-python-662b74bf4b3e