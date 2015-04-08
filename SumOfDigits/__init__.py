def getTuple(file):
    line = file.readline()
    tuple = line.split()
    return tuple
def getSum(tuple):
    sum = 0
    result = int(tuple[0]) * int(tuple[1]) + int(tuple[2])
    result = [int(i) for i in str(result)]
    for num in result:
        sum += num
    return sum
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (getSum(getTuple(file)))
    iter -= 1