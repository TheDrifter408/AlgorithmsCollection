def angryProfessor(k,arr):
    onTime = []
    for i in range(len(arr)):
        if(arr[i] <= 0):
            onTime.append(arr[i])
    if(len(onTime) < k):
        return "YES"
    else:
        return "NO"

print(angryProfessor(4,[-1,-3,4,2]))
