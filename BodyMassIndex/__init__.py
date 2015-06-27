def get_pair(file):
    line = file.readline()
    pair = line.split()
    return pair


def get_bmi(pair):
    BMI = int(pair[0]) / float(pair[1])**2
    return BMI


def get_label(BMI):
    if BMI < 18.5:
        return 'Under'
    if BMI < 25.0:
        return 'Normal'
    if BMI < 30.0:
        return 'Over'
    return 'Obese'


file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(get_label(get_bmi(get_pair(file))))
    iter -= 1
