def birthdayCakeCandles(arr):
    #sort the array
    arr.sort()
    arr.reverse()
    maximum = arr[0]
    maximumCount = 0
    for i in range(len(arr)):
        if(arr[i]>= maximum):
            maximumCount = maximumCount + 1
        else:
            break
    return maximumCount

birthdayCakeCandles([18,90,90,13,90,75,90,8,90,43])