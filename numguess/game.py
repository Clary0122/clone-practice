import random

user_name = input('Enter your name: ')
answer = random.randint(1,100)

# for debugging.
print(answer)

guess = int(input('welcome {}. Guess the number: '.format(user_name)))

n=1

while (n!=3):
    if guess != answer:
        n += 1
        print('wrong!! Try again')
        guess = int(input('Guess the number: '))
        if n==3:
            print('Wrong!! The answer was {}'.format(answer))
    else:
        print('Correct!')
        break

