items = ['Áo tắm', 'Áo mưa', 'Áo khô'] # initialize


def list_out_item():
  for i in range(len(items)):
    print(f'{i+1}.{items[i]}')

while True:
  action = input('Welcome to our shop what do you want? (C R U D): - enter exit to exit')
  action = action.upper()
  if action == 'C':
    new_item = input('Enter new stuff: ')
    items.append(new_item)
    list_out_item()
  elif action == 'R':
    list_out_item()
  elif action == 'U':
    index = int(input('Enter position you want to edit: ')) - 1 
    if index < len(items):
      new_value = input('Enter new value')
      items[index] = new_value
      list_out_item()
    else:
      print('item not in list')
  elif action == 'D':
    remove_value = input('Enter name of the item you want to delete: ')
    if remove_value in items: # check if item have a value in it
      items.remove(remove_value)
      list_out_item()
    else:
      print('item not found')
  elif action == 'EXIT':
    break