def jumpingOnClouds(arr):
    thunderclounds = []
    cumulus = []
    for i in range(len(arr)):
        if(arr[i] == 1):
            thunderclounds.append(i)
        else:
            cumulus.append(i)
    index = 0
    jumps = 0
    print(thunderclounds)
    print(cumulus)
    count = 0
    for i in range(len(cumulus)-1):
        count += 1
    print(count) 
#jumpingOnClouds([0,0,1,0,0,1,0])

jumpingOnClouds([0,0,0,0,1,0])
        

