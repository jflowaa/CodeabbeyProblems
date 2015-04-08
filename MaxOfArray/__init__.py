def getArray(file):
    line = file.readline()
    return line.split()
def getMax(array):
    return max(array)
def getMin(array):
    return min(array)
file = open('arrayData.txt', 'r')
array = [int(i) for i in getArray(file)]
print (getMax(array), getMin(array))