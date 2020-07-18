
# print('hehe')
# print('hoho')
# for i in range(100, -1, -1):
#   print(i, end=' ')
# print(*range(100, -1, -1))

number = int(input('enter a number '))

a = ''
for i in range(0, number+1):
  print(i)
  a = a + str(i)
  print(a)
print(a)