def doCalc(list, result):
    list = list.split()
    if list[0] == '+':
        result += int(list[1])
    elif list[0] == '*':
        result *= int(list[1])
    else:
        result %=  int(list[1])
    return result
with open('data.txt', 'r') as file:
    result = int(file.readline())
    for line in file:
        result = doCalc(line, result)
    print(result)