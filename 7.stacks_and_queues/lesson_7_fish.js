function solution(A, B) {
    let fish = Array.from(Array(A.length), () => new Array(2));
    for(let i = 0; i < A.length; i++) {
        fish[i][0] = A[i]
        fish[i][1] = B[i]
    }

    for(let i = 0; i < A.length - 1; i++) {
        let fish1 = fish[i]
        let fish2 = fish[i+1]
        if(fish2 == undefined || fish1 == undefined) return fish.length
        if(fish1[1] == 1 && fish2[1] == 0) {
            if(fish1[0] > fish2[0]) {
                fish.splice(i + 1, 1)
            } else {
                fish.splice(i, 1)
                if(i > 0) {
                    i--
                }
            }
            i--
        }
    }
    
    return fish.length
}

// first solution is giving 75% at perf
// second solution - using stack

function solution(A, B) {
    let stack = new Array()
    for(let i = 0; i < A.length; i++) {
        if(stack.length == 0) {
            stack.push([A[i], B[i]])
        } else {
            let fish = stack[stack.length - 1]
            let insert = true
            while(fish[1] == 1 && B[i] == 0) {
                if(fish[0] < A[i]) {
                    stack.pop()
                    if(stack.length == 0) break
                    fish = stack[stack.length - 1]
                } else {
                    insert = false
                    break
                }
            } 
            if(insert) {
                stack.push([A[i], B[i]])
            }
        }
    }
    return stack.length
}