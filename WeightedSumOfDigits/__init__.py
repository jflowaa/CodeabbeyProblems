def get_list(file):
    line = file.readline()
    list = line.split()
    return list


def weightedsumofdigits(number):
    weight = 1
    total = 0
    for digit in number:
        total += weight * int(digit)
        weight += 1
    return total

file = open('data.txt', 'r')
iter = int(file.readline())
list = get_list(file)
for item in list[:iter]:
    print(weightedsumofdigits(item))
