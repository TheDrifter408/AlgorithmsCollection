def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    #sort the list
    arr.sort()
    #minimum sum
    for i in range(len(arr)-1):
        minimum = minimum + arr[i]
    for i in range(1,len(arr)):
        maximum = maximum + arr[i]
    print(minimum,maximum)

miniMaxSum([1,3,5,7,9])