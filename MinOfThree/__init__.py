def get_pairofthree(file):
    line = file.readline()
    pairofthree = line.split()
    return pairofthree


def get_min(pairofthree):
    return min(int(pairofthree[0]), int(pairofthree[1]), int(pairofthree[2]))


file = open('minListOfThree.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(get_min(get_pairofthree(file)))
    iter -= 1
