import math
def multipleOfFive(number):
    if(number % 5 == 0):
        return (math.floor(number/5) * 5)
    else:
        return (math.floor(number/5) * 5) + 5

def gradingStudents(grades):
    newGrades = []
    for i in range(len(grades)):
        if(grades[i] < 37):
            newGrades.append(grades[i])
        else: 
            if(multipleOfFive(grades[i]) - grades[i] >= 3):
                newGrades.append(grades[i])
            else:
                newGrades.append(multipleOfFive(grades[i]))
    return newGrades

print(gradingStudents([73,67,38,33]))            



