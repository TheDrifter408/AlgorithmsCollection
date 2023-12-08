def pageCount(n,p):
    #Array of the pages 
    pages = []
    beginningPages = 0
    endingPages = 0
    limit = 0
    if(n % 2 == 0):
        limit = n + 1
    else:
        limit = n
    for i in range(0,limit,2):
        if(i < limit):
            pages.append([i,i+1])
            
        else:
            pages.append([i,0])
    # from the front 
    for i in range(len(pages)):
        if(pages[i][0] == p or pages[i][1] == p):
            beginningPages = i 
            break
        else:
            continue
    # Reverse the pages
    pagesReverse = pages.copy()
    pagesReverse.reverse()
    for i in range(len(pages)):
        if(pagesReverse[i][0] == p or pagesReverse[i][1] == p):
            endingPages = i 
            break
        else:
            continue
    return min(beginningPages,endingPages)  

pageCount(5,4)