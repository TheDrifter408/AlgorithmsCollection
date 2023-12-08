def passwordCracker(arr,stringArr):
    positions = []
    for i in stringArr:
        for j in range(len(arr)):
            pos = arr.index(i)
            positions.append(pos)
    print(positions)

passwordCracker(['because','can','do','must','we','what'],'wedowhatwemustbecausewecan')