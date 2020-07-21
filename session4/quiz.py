quizzes = [
  {
    'question': 'con nhện có mấy chân?',
    'choices': [3, 4, 5, 6],
    'right_choice': 3
  },
  {
    'question': 'con chó có mấy chân?',
    'choices': [3, 4, 5, 6],
    'right_choice': 1
  }, 
  {
    'question': 'con chó có mấy chân?',
    'choices': [3, 4, 5, 6],
    'right_choice': 1
  }
]

right_choices_count = 0

for quiz in quizzes:
  print(quiz['question'])
  for i in range(len(quiz['choices'])):
    print(f' {i+1}. {quiz["choices"][i]} ')

  your_choice = int(input('your choice: ')) - 1
  if your_choice == quiz['right_choice']:
    right_choices_count = right_choices_count + 1
  else:
    print('sai mất r :((')

correct_percent = right_choices_count / len(quizzes) * 100
print(f'{correct_percent}%')