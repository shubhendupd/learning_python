import sys

print('Welcome to the Quiz Game!')

playing = input('Do you want to play? (yes/no): ')
if playing.lower() != 'yes':
    print('Maybe next time!')
    sys.exit()

print('Great! Let\'s start the quiz.')

answer = input(" what does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print('Correct!')
else:
    print('Incorrect!')
