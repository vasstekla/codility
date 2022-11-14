function solution(H) {
    let blocks = 0
    let stack = new Array()
    stack.push(H[0])

    for(let i = 1; i < H.length; i ++) {
        if(stack.length == 0) {
            stack.push(H[i])
        } else {
            let top = stack[stack.length - 1]
            while(top > H[i]) {
                stack.pop()
                blocks++
                if(stack.length == 0) {
                    break
                }
                top = stack[stack.length - 1]
            }
            if(stack.length == 0 || top < H[i]) {
                stack.push(H[i])
            }
        }
    }
    return blocks + stack.length
}