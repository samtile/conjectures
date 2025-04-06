import math

# Aaron's base 5 conjecture
def aaronBaseFiveConjecture():
    currentNumber = 4579847
    sequence = [None] * 100
    sequence[0] = currentNumber
    currentIndex = 1
    while(True):
        if (currentNumber % 5 == 0):
            sequence[currentIndex] = normal_round(currentNumber/5)
        elif (currentNumber % 5 == 1):
            sequence[currentIndex] = normal_round(currentNumber/2)
        elif (currentNumber % 5 == 2):
            sequence[currentIndex] = (currentNumber*2)-3
        elif (currentNumber % 5 == 3):
            sequence[currentIndex] = normal_round((currentNumber*3)/4)-1
        else:
            sequence[currentIndex] = normal_round((currentNumber*3)/5)
        currentNumber = sequence[currentIndex]
        currentIndex+=1
        if currentNumber==1 or currentIndex==99:
            break
    for i in range(currentIndex):
        print(sequence[i])

def normal_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

aaronBaseFiveConjecture()
