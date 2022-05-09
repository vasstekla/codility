def solution(A):
    s = len(A)
    count = 0

    for i in range(s-1):
        for j in range(i+1, s):
            if(j-i <= A[i] + A[j]):
                count+=1
    
    if(count > 10000000):
        return -1
    
    return count

#the solution above is 100% correct however gets 12% at performance
#the following solution was inspired by https://medium.com/@deck451/codility-algorithm-practice-lesson-6-sorting-task-4-number-of-disc-intersections-a-python-378a296e760d
#I couldn't get by the end of it on my own, 
#since for me it didn't cross my mind to separate the starting and the ending points in a way that you lose the connection between them

def solution(A):
    s = len(A)
    starting_points = [0]*s
    ending_points = [0]*s

    for i in range(s):
        starting_points[i] = i - A[i]
        ending_points[i] = i + A[i]

    starting_points.sort()
    ending_points.sort()
    k = 0
    count = 0
    open_disc = 0

    for i in range(s):
        for j in range(k, s):
            if starting_points[i] <= ending_points[j]:
                count += open_disc
                if count > 10000000:
                    return -1
                open_disc += 1
                break
            open_disc -= min(1, open_disc)
            k += 1
                

    return count