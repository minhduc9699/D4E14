number_of_1_0 = int(input('enter the total of 1 and 0: '))
for i in range(number_of_1_0):
  if i % 2 == 0:
    print('1', end=' ')
  else:
    print('0', end=' ')