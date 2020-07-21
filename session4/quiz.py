quiz = {
  'question': 'con nhện có mấy chân?',
  'choices': [3, 4, 5, 6],
  'right_choice': 3
}

print(quiz['question'])
for i in range(len(quiz['choices'])):
  print(f' {i+1}. {quiz["choices"][i]} ')