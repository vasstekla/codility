function solution(A) {
    let peaks = new Array()

    for(let i = 1; i < A.length - 1; i++) {
        if(A[i - 1] < A[i] && A[i] > A[i + 1]) {
            peaks.push(i)
        }
    }

    if(peaks.length == 0) {
        return 0
    }

    if(peaks.length == 1) {
        return 1
    }


    let maxFlags = peaks.length
    let maxFlagsPutDown = 2
    let possible = true

    while(possible && maxFlagsPutDown <= maxFlags) {
        possible = false
        let flags = maxFlagsPutDown - 1
        let lastFlagIndex = 0
        for(let i = 1; i < peaks.length; i++) {
            if(peaks[i] - peaks[lastFlagIndex] >= maxFlagsPutDown) {
                flags--
                lastFlagIndex = i
                if(flags == 0) {
                    possible = true
                    maxFlagsPutDown ++
                    break
                }
            }
        }
    }
    return maxFlagsPutDown - 1
}