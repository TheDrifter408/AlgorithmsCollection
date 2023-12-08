def circularArrayRotation(arr,k,queries):
    result = []
    for i in range(k):
        lastEl = arr.pop()
        arr.insert(0,lastEl)
    for i in range(len(queries)):
        result.append(arr[queries[i]])
    return result
circularArrayRotation([1,2,3],2,[0,1,2])
