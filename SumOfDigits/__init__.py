def get_pairofthree(file):
    line = file.readline()
    pairofthree = line.split()
    return pairofthree


def get_sum(pairofthree):
    sum = 0
    result = int(pairofthree[0]) * int(pairofthree[1]) + int(pairofthree[2])
    result = [int(i) for i in str(result)]
    for num in result:
        sum += num
    return sum


file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(get_sum(get_pairofthree(file)))
    iter -= 1
