def getList(file):
    line = file.readline()
    list = line.split()
    return list
def calc(temp):
    return (temp - 32) * (5.0/9.0)
file = open('data.txt', 'r')
list = getList(file)
iter = int(list[0]) + 1
for temp in list[1:iter]:
    print (round(calc(int(temp))))