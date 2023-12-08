def timeConversion(str):
    twelveHourArr = str.split(":")
    twentyFourHourArr = []
    intTimeArr = []
    PMorAM = ""
    twentyFourHour = ""
    #get PM or AM 
    for i in range(2,len(twelveHourArr[len(twelveHourArr)-1])):
        PMorAM += twelveHourArr[2][i]
    # remove last element from stringTimeArr
    lastElement = twelveHourArr.pop()
    tempString = ""
    for i in range(0,2):
        tempString += lastElement[i]
    twelveHourArr.append(tempString)
    for i in range(len(twelveHourArr)):
        intTimeArr.append(int(twelveHourArr[i]))
    if(PMorAM == "PM"):
        if(intTimeArr[0] < 12):
            intTimeArr[0] = intTimeArr[0] + 12
    else:
        if(intTimeArr[0] == 12):
            intTimeArr[0] = 0
    print(intTimeArr)
    # convert time in int to string
    if(intTimeArr[0] >= 12):
        tempStr = ""
        tempStr = f'{intTimeArr[0]}'
        twentyFourHourArr.append(tempStr)
    else:
        tempStr = ""
        tempStr += "0" + f'{intTimeArr[0]}'
        twentyFourHourArr.append(tempStr)
    if(intTimeArr[1] > 9):
        tempStr = f'{intTimeArr[1]}'
        twentyFourHourArr.append(tempStr)
    else:
        tempStr = ""
        tempStr += "0" + f'{intTimeArr[1]}'
        twentyFourHourArr.append(tempStr)
    if(intTimeArr[2] > 9):
        tempStr = f'{intTimeArr[2]}'
        twentyFourHourArr.append(tempStr)
    else:
        tempStr = ""
        tempStr += "0" + f'{intTimeArr[2]}'
        twentyFourHourArr.append(tempStr)
    twentyFourHourArr.append(PMorAM)
    twentyFourHour = f'{twentyFourHourArr[0]}:{twentyFourHourArr[1]}:{twentyFourHourArr[2]}'
    return twentyFourHour

timeConversion("12:45:54PM")