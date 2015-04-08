import math
def getFactor(file):
    return file.readline()
def getResult(factor):
    roll = math.floor(6 * float(factor)) + 1
    return roll
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (getResult(getFactor(file)))
    iter -= 1