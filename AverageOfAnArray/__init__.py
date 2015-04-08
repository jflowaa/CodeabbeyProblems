def getList(file):
    line = file.readline()
    return line.split()
def avgOfArray(list):
    avg = 0
    for num in range(len(list) - 1):
        avg += int(list[num])
    return avg/(len(list)-1)
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (round(avgOfArray(getList(file))))
    iter -= 1