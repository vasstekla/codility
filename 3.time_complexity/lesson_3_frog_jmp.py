def solution(X, Y, D):
    distance = Y - X
    if(distance % D == 0):
        return int(distance / D)
    return int((Y-X) / D) + 1