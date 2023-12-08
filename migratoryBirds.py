def migratoryBirds(arr):
    arr.sort()
    results = []
    print(arr)
    for i in range(len(arr),2):
        count = 0
        if(arr[i] == arr[i + 1]):
            print(arr[i],arr[i+1])
            count += 1
        results.append(count)
    print(results)
    
migratoryBirds([1,2,3,4,5,4,3,2,1,3,4])