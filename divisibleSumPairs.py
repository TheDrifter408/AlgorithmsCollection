def divisibleSumPairs(n,k,arr):
    pairs = []
    for i in range(0,n):
        for j in range(i+1,n):
            tempNum = arr[i] + arr[j]
            if(tempNum % k == 0):
                pairs.append((arr[i],arr[j]))
    return len(pairs)

divisibleSumPairs(6,3,[1,3,2,6,1,2])
    
