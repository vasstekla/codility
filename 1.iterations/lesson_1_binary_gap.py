def solution(N):
    binary_number = bin(N)
    found_one = False
    current_count = 0
    max_count = 0
    for i in binary_number:
        if(i == '1'):
            if(found_one == False):
                found_one = True
            else:
                if(current_count > max_count):
                    max_count = current_count
                current_count = 0
        elif(i == '0' and found_one == True):
            current_count = current_count + 1
        else:
            current_count = 0
    return max_count