def solution(S):
    s = len(S)
    stack = [''] * s
    top = 0

    brackets = {'{' : '}', '[' : ']', '(' : ')'}

    if(s == 0):
        return 1

    for elem in S:
        if (elem == '{' or elem == '[' or elem == '('):
            #push
            stack[top] = elem
            top += 1
        else:
            #pop
            if(top == 0):
                return 0
            if(brackets[stack[top-1]] != elem):
                return 0
            top -= 1

    if(top == 0):
        return 1
    return 0