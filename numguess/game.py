import random


user_name = input('Enter your name: ')
answer = random.randint(1,100)

# for debugging.
print(answer)

guess = int(input('Welcome, {}. Guess the number! : '.format(user_name)))

# for debugging.
print(answer, guess, type(guess))

if guess==answer:
    print('Correct!!')
else:
    print('Wrong!!! The answer was {}.'.format(answer))

