import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
list=['tails','heads']
if list[toss] == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    toss = random.randint(0, 1)
    if list[toss] == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

