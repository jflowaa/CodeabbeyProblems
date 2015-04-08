def readWords(file):
    return file.readline()
file = open('data.txt', 'r')
words = readWords(file)
print (words[::-1])