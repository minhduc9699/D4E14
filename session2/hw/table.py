n = int(input())

for y in range(1, n+1):
  for x in range(1, n+1):
    if x * y >= 10:
      print(x * y, end=' ')
    else:
      print(x * y, end='  ')
  print()