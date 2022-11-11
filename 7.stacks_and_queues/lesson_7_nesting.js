function solution(S) {
    let stack = new Array()
    for (let i = 0; i < S.length; i++) {
        switch(S[i]) {
            case ')':
                if(stack.length < 0 || stack.pop() != '(') {
                    return 0
                }
                break
            default:
                stack.push(S[i])
                break
        }
    }
    if(stack.length == 0) {
        return 1
    }
    return 0
}