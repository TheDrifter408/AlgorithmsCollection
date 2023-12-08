import math
def powerSum(X,N):
    limit = math.ceil(math.sqrt(X))
    print(limit)
    pairs = []
    for i in range(1,limit+1):
        for j in range(i+1,limit+1):
            if((pow(i,N) + pow(j,N)) == X):
                pairs.append((i,j))
    print(pairs)
powerSum(100,3)