import math


def get_factor(file):
    return file.readline()


def get_result(factor):
    roll = math.floor(6 * float(factor)) + 1
    return roll


file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(get_result(get_factor(file)))
    iter -= 1
