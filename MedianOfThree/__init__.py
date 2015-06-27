def get_pairofthree(file):
    line = file.readline()
    pairofthree = line.split()
    return [int(i) for i in pairofthree]


def getMedian(pairofthree):
    pairofthree.sort()
    return int(pairofthree[1])


file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(getMedian(get_pairofthree(file)))
    iter -= 1
