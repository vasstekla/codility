def solution(S):
    s = len(S)
    open_brackets = 0
    close_brackets = 0

    for elem in S:
        if(elem == '('):
            open_brackets += 1
        else:
            close_brackets += 1
    
    if(open_brackets != close_brackets):
        return 0

    stack = [''] * s
    top_elem_index = 0

    for index in range(s):
        if(S[index] == '('):
            stack[top_elem_index] = S[index]
            top_elem_index += 1
        else: 
            if(top_elem_index == 0):
                return 0
            top_elem_index -= 1
    return 1