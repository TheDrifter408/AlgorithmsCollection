def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for i in range(len(arr)):
        if(arr[i]>=1):
            positive = positive + 1
        elif (arr[i] < 0):
            negative = negative + 1
        elif (arr[i] == 0):
            zeros = zeros + 1
    positive_ratio = positive / len(arr) 
    negative_ratio = negative / len(arr)
    zeros_ratio = zeros / len(arr)
    print("%.6f" % positive_ratio)
    print("%.6f" % negative_ratio)
    print("%.6f" % zeros_ratio)

arr = [1,1,0,-1,-1]
plusMinus(arr)