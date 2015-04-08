def sumLoop(list, iter):
    total = 0
    for item in range(iter(list)):
        total += item
    return total
iter = input('Enter amount of times to iterate: ')
numbers = map(int, input('Paste the list numbers: ').split())
print (sum(numbers))