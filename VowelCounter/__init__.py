def get_line(file):
    line = file.readline()
    return line


def count_vowels(line):
    count = 0
    for char in list(line):
        if char.lower() in vowels:
            count += 1
    return count


vowels = ['a', 'e', 'i', 'o', 'u', 'y']
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print(count_vowels(get_line(file)))
    iter -= 1
