def getTuple(file):
    line = file.readline()
    tuple = line.split()
    return tuple
def getMin(tuple):
    return min(int(tuple[0]), int(tuple[1]), int(tuple[2]))
file = open('minListOfThree.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (getMin(getTuple(file)))
    iter -= 1