def getPair(file):
    line = file.readline()
    pair = line.split()
    return pair
def addPair(pair):
    return int(pair[0]) + int(pair[1])
file = open('sumListedPairs.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (addPair(getPair(file)))
    iter -= 1