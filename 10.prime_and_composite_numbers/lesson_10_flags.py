def solution(A):
    n = len(A)

    if(n < 3):
        return 0

    #lets map the peaks, if it's 1 then it's a peak, if 0 then not
    peaks = [0]*n
    peaks[0] = 0  
    peak_count = 0  
    first_peak_index = -1
    last_peak_index = -1

    for index in range(1, n-1):
        if(A[index] > A[index - 1] and A[index] > A[index + 1]):
            if(first_peak_index == -1):
                first_peak_index = index
            last_peak_index = index
            peak_count += 1
            peaks[index] = 1
            peaks[index + 1] = 0
            index += 1
        
    if(peak_count < 2):
        return peak_count

    distance_sqrt = int((last_peak_index - first_peak_index)**(1/2))
    flags_try = peak_count
    
    if(distance_sqrt < peak_count):
        flags_try = distance_sqrt+1
    
    while(flags_try != 0):
        flag = flags_try

        i = first_peak_index
        while(i < last_peak_index + 1):
            if(peaks[i] == 1):
                flag -= 1
                if(flag == 0):
                    return flags_try
                i += flags_try
            else:
                i += 1
        flags_try -= 1

    return 0

#finally solved

def solution(A):
    n = len(A)

    if(n < 3):
        return 0

    #lets map the peaks, if it's 1 then it's a peak, if 0 then not
    peaks = [0]*n
    peaks[0] = 0  
    first_peak_index = -1
    last_peak_index = -1

    #optimalized - we not simply mark the peaks but mark the next peak 
    for index in range(n-2, 0, -1):
        if(A[index] > A[index - 1] and A[index] > A[index + 1]):
            if(last_peak_index == -1):
                last_peak_index = index
            first_peak_index = index
            peaks[index] = index
        else:
            peaks[index] = peaks[index + 1]

    flags_try = int((last_peak_index - first_peak_index)**(1/2)) + 1
    
    while(flags_try != 0):
        flag = flags_try
        i = first_peak_index
        while(i < last_peak_index + 1):
            if(peaks[i]):
                i = peaks[i]
                flag -= 1
                if(flag == 0):
                    return flags_try
                i += flags_try
            else:
                i += 1
        flags_try -= 1

    return 0