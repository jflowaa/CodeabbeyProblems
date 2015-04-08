def getList(file):
    line = file.readline()
    list = line.split()
    return list
def getSequence(number):
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number /2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    return count
file = open('data.txt', 'r')
iter = int(file.readline())
list = [int(i) for i in getList(file)]
for i in range(iter):
    print (getSequence(list[i]))