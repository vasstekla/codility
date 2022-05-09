def solution(H):
    lenght = len(H)
    stack = [0]*lenght
    stack[0] = H[0]
    top_index = 1
    cubes = 1

    for index in range(1, lenght):
        if(top_index != 0):
            if(stack[top_index - 1] > H[index]):
                while(top_index != 0 and stack[top_index - 1] > H[index]):
                    top_index -= 1
                    stack[top_index] = 0
                    cubes += 1
        if(stack[top_index - 1] != H[index]):
            stack[top_index] = H[index]
            top_index += 1

    return cubes + top_index - 1

#got 100% on my own yaaay!