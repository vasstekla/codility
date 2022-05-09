def solution(N, A):
    counters_last_place = [0] * N
    max_value = 0
    for operation in A:
        if(operation > N):
            counters_last_place = [max_value] * N
        elif(operation >= 1):
            counters_last_place[operation - 1] += 1
            if max_value < counters_last_place[operation - 1]:
                max_value = counters_last_place[operation - 1]
    return counters_last_place

#the above solution gives a 88% total score, because of the performance issue at line 6
#after some google search I modified it to be 100% (although I am not happy with it xD)

def solution(N, A):
    counters_last_place = [0] * N
    max_value = 0
    all_max_value = 0
    for operation in A:
        if(operation > N):
            all_max_value = max_value
        elif(operation >= 1):
            if(counters_last_place[operation - 1] < all_max_value):
                counters_last_place[operation - 1] = all_max_value
            counters_last_place[operation - 1] += 1
            if max_value < counters_last_place[operation - 1]:
                max_value = counters_last_place[operation - 1]
    for i, elem in enumerate(counters_last_place):
        if (elem < all_max_value):
            counters_last_place[i] = all_max_value
    return counters_last_place