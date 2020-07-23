sheep_size = [4, 47, 34, 346, 32, 25, 90]

def shear():
  max_sheep_size = sheep_size[0]
  for size in sheep_size:
    if size > max_sheep_size:
      max_sheep_size = size
  max_sheep_size_index = sheep_size.index(max_sheep_size) # find index by value
  sheep_size[max_sheep_size_index] = 8
  print(f'now my biggest sheep size is {max_sheep_size}, lets shear it')
  print('after shearing here my flock: ')
  print(sheep_size, sep=' ')

def grow():
  new_sheep_size = []
  for size in sheep_size:
    new_sheep_size.append(size + 50)
  print('One month has passed, now here my flock')
  print(new_sheep_size)

def sell():
  total_size = sum(sheep_size)
  sell_money = total_size * 2
  print('My flock have size in total', total_size)
  print(f'i would get {total_size} * 2$ = {sell_money}$')


print('*' * 20)
print('hello, my name is Duc, and here is my flock: ')
print(sheep_size)
print('\n')
shear()
print('\n')
for i in range(4):
  grow()
  shear()
  print('\n')
sell()
