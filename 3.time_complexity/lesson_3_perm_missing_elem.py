def solution(A):
    occurrence_list = [False] * (len(A)+1)
    for i in A:
        occurrence_list[i-1] = True
    for index, elem in enumerate(occurrence_list):
        if(elem == False):
            return index+1