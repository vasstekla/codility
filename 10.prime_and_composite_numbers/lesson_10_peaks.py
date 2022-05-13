def solution(A):
    n = len(A)
    peaks = [n]*n
    peak_count = 0

    for i in range(n-2, 0, -1):
        if(A[i] > A[i-1] and A[i] > A[i+1]):
            peak_count += 1
            peaks[i] = i
        else:
            peaks[i] = peaks[i + 1]

    if(peak_count < 2):
        return peak_count
    
    peaks[0] = peaks[1]

    lenght_try = peak_count

    while(lenght_try != 0):
        lenght_try_curr = lenght_try
        if(n % lenght_try_curr == 0):
            i = 0
            sections = int(n / lenght_try_curr)
            while(i < n):
                #if we have a peak in the section
                if(peaks[i] < i + sections):
                    lenght_try_curr -= 1
                    i += sections
                    if(lenght_try_curr == 0):
                        return lenght_try
                else:
                    break
                
        lenght_try -= 1
                
    return 0