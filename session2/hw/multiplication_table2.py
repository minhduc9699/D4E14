num = int(input('enter a number:'))


for row in range (num):
    for column in range(num):
      if (row + column) % 2 == 0:
        print(1, end='  ')
      else:
        print(0, end='  ')
    print('\n')
