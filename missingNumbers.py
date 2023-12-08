def missingNumbers(arr,brr):
    alt_arr = arr.copy()
    alt_brr = brr.copy()
    alt_arr.sort()
    alt_brr.sort()
    print(alt_arr)
    print(alt_brr)
    freq_arr = []
    count = 0
    for i in range(len(alt_arr)):
        count = 0
        for j in range(i+1,len(alt_arr)):
            if(alt_arr[i] == alt_arr[j]):
                count += 1
        if(count <= 1):
            continue
        else:    
            freq_arr.append((alt_arr[i],count))
    print(freq_arr)

missingNumbers([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204])