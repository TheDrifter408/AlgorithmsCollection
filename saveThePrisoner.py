def saveThePrisoner(n,m,s):
    chairs = []
    if(s == 1):
        for i in range(s,n+1):
            chairs.append(i)
    else:
        for i in range(s,n+1):
            chairs.append(i)
        for j in range(s-1,n):
            chairs.append(j)
    if(m <= len(chairs)):
        print(chairs[m-1])
        #return chairs[m-1]
    else:
        remainderCandies = m % n
        print(chairs[remainderCandies-1])
        #return chairs[remainderCandies-1]
saveThePrisoner(7,19,2)
