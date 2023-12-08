def diagonalDifference(arr):
    leftDiagonal = 0
    rightDiagonal = 0
    diff_diagonal = 0
    # Left Diagonal
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(i == j):
                leftDiagonal += arr[i][j]
    # Right Diagonal
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if((i + j) == len(arr) - 1):
                rightDiagonal += arr[i][j]

    diff_diagonal = abs(leftDiagonal - rightDiagonal)
    return diff_diagonal
diagonalDifference()
