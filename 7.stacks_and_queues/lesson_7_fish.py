def solution(A, B):
    s = len(A)
    fight = True
    current_fish_index = 0
    last_fish_index = s-1

    while(fight):
        fight = False
        while(current_fish_index != last_fish_index):
            #if they meet
            if(B[current_fish_index] == 1 and B[current_fish_index + 1] == 0):
                    fight = True
                    last_fish_index -= 1
                    #we measure their size
                    if(A[current_fish_index] > A[current_fish_index + 1]):
                        A.pop(current_fish_index + 1)
                        B.pop(current_fish_index + 1)
                    else:
                        A.pop(current_fish_index)
                        B.pop(current_fish_index)
                        break
            else:
                current_fish_index += 1
        if(fight == True):
            current_fish_index = 0
    
    return last_fish_index + 1

#this was my first try - 100% correctness however only 50% performance because it is O(n**n)

#solution with stack from https://programming-review.com/python/algorithms#fish, which is O(n)

def solution(a, b):
    l = 0 # left
    s = [] # stack
    for i in range(len(a)):
        if b[i]==1: # fish moving upwards
            s.append(a[i]) # to the stack
        else: # eat fish mowing downwards.
            while len(s)>0:
                if s[-1]<a[i]:
                    s.pop() # eat from the stack
                else:
                    break
            else:
                l+=1
    l+=len(s)
    return l