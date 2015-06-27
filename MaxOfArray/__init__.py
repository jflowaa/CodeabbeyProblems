def get_array(file):
    line = file.readline()
    return line.split()


def get_max(array):
    return max(array)


def get_min(array):
    return min(array)


file = open('arrayData.txt', 'r')
array = [int(i) for i in get_array(file)]
print(get_max(array), get_min(array))
