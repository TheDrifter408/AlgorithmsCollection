def staircase(n):
    res_string = ""
    #add spaces 
    for i in range(n):
        spaces = n - i - 1
        hashes = 1 + i
        # add spaces
        for j in range(spaces):
            res_string += " "
        #add hashes
        for k in range(hashes):
            res_string += "#"
        if(i == n - 1):
            res_string += ""
        else:
            res_string += '\n'
    print(res_string)

staircase(6)