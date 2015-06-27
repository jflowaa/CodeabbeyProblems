def get_pair(file):
    line = file.readline()
    pair = line.split()
    return pair


def get_min(pair):
    return min(int(pair[0]), int(pair[1]))


file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(get_min(get_pair(file)))
    iter -= 1
