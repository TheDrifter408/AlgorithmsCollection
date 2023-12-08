def hurdleRace(k,height):
    arr = height.copy()
    arr.sort()
    if( k < arr[len(arr) - 1]):
        return arr[len(arr) - 1] - k
    else:
        return 0
    
print(hurdleRace(4,[1,6,3,5,2]))