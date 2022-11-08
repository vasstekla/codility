function solution(N) {
    if(N == 0) return 0

    let binary = N.toString(2)
    let longestBinGap = 0
    let currentBinGap = 0

    for(let i = 1; i < binary.length; i++) {
        if(binary[i] == '0') {
            currentBinGap ++
        } else {
            if(currentBinGap > longestBinGap) {
                longestBinGap = currentBinGap
            }
            currentBinGap = 0
        }
    }

    return longestBinGap
}