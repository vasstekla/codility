# got a bit of inspiration from https://app.codility.com/demo/results/trainingR7UKQB-9AQ/
#before this I've never used zip, which helped quite a lot

def planks_for_nails(nail, planks_sorted):
    begin = 0   
    end = len(planks_sorted) - 1
    while(begin <= end):
        mid = int((begin + end)/2)
        if(nail < planks_sorted[mid][0]):
            end = mid - 1
        elif(nail > planks_sorted[mid][1]):
            begin = mid + 1
        else: 
            return mid
    return -1

def solution(A, B, C):
    n = len(C)
    planks_sorted = sorted(zip(A,B))

    for i in range(n):
        nail = C[i]
        plank = planks_for_nails(nail, planks_sorted)
        while plank > -1:
            del planks_sorted[plank]
            plank = planks_for_nails(nail, planks_sorted)
        if not planks_sorted:
            return i + 1

    return -1