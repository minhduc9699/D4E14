person = ['Đức', 96, 175, 70, 'Sơn La', True, False, 1]

# init

person_dict = {
  'yob': 96,
  'height': 175,
  'weight': 70,
  'name': 'Đức',
  'nam': '0'
}
if 'nam' in person_dict: # check if key in dictionary
  print(person_dict['nam']) # Read one
name = person_dict['name']
person_dict['job'] = 'dev' # Create
person_dict['name'] = 'Đạo' # Update
del person_dict['nam'] # Delete
print(person_dict)
for key in person_dict:
  print(key, person_dict[key])
