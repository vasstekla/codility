function solution(A) {
    let n = A.length
    let peaks = new Array(n).fill(0)
    let peakCount = 0

    for(let i = 1; i < n - 1; i++) {
        if(A[i - 1] < A[i] && A[i] > A[i + 1]) {
            peaks[i] = 1
            peakCount ++
        }
    }
    if (peakCount == 0) {
        return 0
    }

    if (peakCount == 1) {
        return 1
    }

    let blocks = peakCount

    while(blocks > 0) {
        if(n % blocks == 0) {
            let blocksLength = n / blocks
            let blockEnd = blocksLength 
            let i = 0
            let foundFlag = false
            
            while(i < n) {
                foundFlag = false
                if(i < blockEnd) {
                    if(peaks[i] == 1) {
                        foundFlag = true
                        i = blockEnd
                        blockEnd += blocksLength
                    } else {
                        i++
                    }
                } else {
                    break
                }
            }    
            if(i >= n && foundFlag) {
                return blocks
            }     
        }
        blocks --
    }

    return blocks
}