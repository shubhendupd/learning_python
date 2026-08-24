import sys

print('Welcome to the Quiz Game!')
score = 0

playing = input('Do you want to play? (yes/no): ')
if playing.lower() != 'yes':
    print('Maybe next time!')
    sys.exit()

print('Great! Let\'s start the quiz.')

answer = input(" what does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input(" what does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input(" what does RAM stand for? ")
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input(" what does psu stand for? ")
if answer.lower() == 'power supply unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


answer = input(" what does ups stand for? ")
if answer.lower() == 'uninterruptible power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(' You got ' + str(score) + ' questions correct!')
grade = (score / 5) * 100
print('Your grade is: ' + str(grade) + '%')