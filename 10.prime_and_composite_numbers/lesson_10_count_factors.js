function solution(N) {
    let divisors = 0
    let i = 1

    while(i < Math.sqrt(N)) {
        if(N % i == 0) {
            divisors += 2
        }
        i ++
    }

    if(i == Math.sqrt(N)) {
        divisors ++
    }

    return divisors
}