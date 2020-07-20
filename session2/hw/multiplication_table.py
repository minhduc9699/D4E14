num = int(input('enter a number:'))

for row in range(1, num + 1):
    for column in range (1, num + 1):
        table = row * column
        print(table, end='  ')
        if table < 10:
            print(end=' ')
    print('\n')
