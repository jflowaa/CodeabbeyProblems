def getTuple(file):
    line = file.readline()
    tuple = line.split()
    return [int(i) for i in tuple]
def getMedian(tuple):
    tuple.sort()
    return int(tuple[1])
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (getMedian(getTuple(file)))
    iter -= 1