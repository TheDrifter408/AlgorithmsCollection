from calendar import monthrange
def dayOfProgrammer(y):
    totaldays = 0
    date = ''
    if(y == 1918):
        date = f'{26}.09.{y}'
    elif(y < 1948):
        if(y % 4 == 0):
            date = f'{12}.09.{y}'
        else:
            date = f'{13}.09.{y}'
    else:
        for i in range(8):
            totaldays += monthrange(y,i+1)[1]
        date = f'{256 - totaldays}.09.{y}'
    return date
dayOfProgrammer(1918)    
