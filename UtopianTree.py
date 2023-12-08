def utopianTree(n):
    initialHeight = 1
    for i in range(n):
        if(i % 2 == 0):
            initialHeight = initialHeight * 2
        else:
            initialHeight = initialHeight + 1
    return initialHeight
    

utopianTree(5)
