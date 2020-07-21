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
  }
]

for quiz in quizzes:
  print(quiz['question'])
  for i in range(len(quiz['choices'])):
    print(f' {i+1}. {quiz["choices"][i]} ')

  your_choice = int(input('your choice: ')) - 1
  if your_choice == quiz['right_choice']:
    print('hurayy!')
  else:
    print('sai mất r :((')