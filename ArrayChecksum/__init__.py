def get_list(file):
    line = file.readline()
    list = line.split()
    return list


def get_check_sum(list):
    result = 0
    for num in list[0:iter]:
        result = ((result + int(num)) * seed) % 10000007
    return result


seed = 113
file = open('data.txt', 'r')
iter = int(file.readline())
print(get_check_sum(get_list(file)))
