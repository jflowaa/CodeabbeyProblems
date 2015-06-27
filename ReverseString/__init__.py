def read_words(file):
    return file.readline()


file = open('data.txt', 'r')
words = read_words(file)
print(words[::-1])
