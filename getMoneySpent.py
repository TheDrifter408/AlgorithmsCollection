def getMoneySpent(keyboards,drives,b):
    combinations = []
    if(len(keyboards) <= len(drives)):
        for i in range(len(keyboards)):
            for j in range(len(drives)):
                if(keyboards[i] + drives[j] <= b):
                    combinations.append(
                        (i,j,abs(
                            10 - (keyboards[i] + drives[j])
                            )
                        )
                    )
    else:
        for i in range(len(drives)):
            for j in range(len(keyboards)):
                if(drives[i] + keyboards[j] < b):
                    combinations.append(
                        (i,j,abs(
                            10 - (keyboards[i] + drives[j])
                            )
                        )
                    )
    # To sort a list of tuples but its third element in the tuple a callback or anonymous function must be used
    print("Before:",combinations)
    combinations.sort(key = lambda a:a[2])
    print("After:",combinations)
    if(len(combinations) == 0):
        return -1
    elif(len(keyboards) <= len(drives)):
        (keyboard,drive,diff) = combinations[0]
        return keyboards[keyboard] + drives[drive]
    else:
        (drive,keyboard,diff) = combinations[0]
        return keyboards[keyboard] + drives[drive]
      

getMoneySpent([3,1],[5,2,8],10)