def getPair(file):
    line = file.readline()
    pair = line.split()
    return pair
def divide(pair):
    return int(pair[0]) / int(pair[1])
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (round(divide(getPair(file))))
    iter -= 1
