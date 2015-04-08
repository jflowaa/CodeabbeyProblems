def getArray(file):
    return file.readline().split()
def bubbleSort(list):
    swaps = 0
    passes = 0
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(0, (len(list)-1)):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swaps += 1
                sorted = False
        passes += 1
    return passes, swaps
file = open('data.txt', 'r')
size = int(file.readline())
print (bubbleSort([int(i) for i in getArray(file)]))