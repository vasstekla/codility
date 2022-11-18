function solution(N) {
    let perimeter = 2 * (1 + N)
    for(let i = 1; i <= Math.sqrt(N); i++) {
        if(N % i == 0) {
            perimeter = Math.min(perimeter, 2 * (i + (N / i)))
        }
    }
    return perimeter
}