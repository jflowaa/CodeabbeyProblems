def getPair(file):
    line = file.readline()
    pair = line.split()
    return pair
def getMin(pair):
    return min(int(pair[0]), int(pair[1]))
file = open('minListedPairs.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (getMin(getPair(file)))
    iter -= 1