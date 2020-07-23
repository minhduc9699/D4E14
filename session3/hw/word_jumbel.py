from random import *
from getpass import getpass

quizz = []
number_of_quizz = int(input('how many quizz do you want? '))
for i in range(number_of_quizz):
    word = getpass('enter your quizz: ')
    quizz.append(word)

playing = True
while playing:
    print(f'lest play, there are {number_of_quizz} quizz')
    for i in range(number_of_quizz):
        random_quizz = quizz[randint(0, len(quizz) - 1)]
        char = list(random_quizz)
        shuffle(char)
        print(*char)
        key = input('enter your awnser: ')
        if key == random_quizz:
            print('Bingo!!')
        else:
            print(':(')
            break
    break
