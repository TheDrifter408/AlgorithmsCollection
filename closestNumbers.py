def closestNumbers(arr):
    arr.sort()
    differences = []
    pairs = []
    final_result = []
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        differences.append((i+1,i,diff))
    differences.sort(key = lambda x: x[2])
    minimumDiff = differences[0][2]
    for i in range(len(differences)):
        if(differences[i][2] == minimumDiff):
            pairs.append(differences[i])
    # print("Differences:")
    # for i in range(len(differences)):
    #     print(differences[i])
    # print("Pairs:",pairs)
    for i in range(len(pairs)):
        (x, y , diff) = pairs[i]
        final_result.append(arr[x])
        final_result.append(arr[y])
    final_result.sort()
    return final_result


closestNumbers([-20,-3916237,-357920,-3620601,7374819,-7330761,30,6246457,-6461594,266854,-520,-470])
#closestNumbers([5,4,3,2])