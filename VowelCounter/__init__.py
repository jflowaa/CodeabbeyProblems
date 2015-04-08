def getLine(file):
    line = file.readline()
    return line
def countVowels(line):
    count = 0
    for char in list(line):
        if char.lower() in vowels:
            count +=1;
    return count
vowels =['a', 'e', 'i', 'o', 'u', 'y']
file = open('data.txt', 'r')
iter = int(file.readline())
while iter > 0:
    print (countVowels(getLine(file)))
    iter -= 1