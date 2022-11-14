function solution(A) {
    let maxProfit = 0
    let minBuy = A[0]
    let maxSell = A[0]

    for(let i = 1; i < A.length; i++) {
        if(minBuy > A[i]) {
            minBuy = A[i]
            maxSell = minBuy
        } else {
            maxSell = Math.max(maxSell, A[i])
            maxProfit = Math.max(maxProfit, maxSell - minBuy)
        }
    }
    
    return maxProfit
}