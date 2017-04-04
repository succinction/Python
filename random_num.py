import random as r
from random import randrange

number = r.randint(1,100)

for i in range(100):
    print(i, r.randrange(100))
    print(i%2 == 0)


'''
using random module assign a variable a random number 1 - 100
using conditionals, while loop and input ask a user to guess the number
if they guess lower than the number tell user thay are low
if they guess high then tell them number is too high.
when they guess the number inform user and exit loop
'''

print('##################################')

number = r.randint(1,100)
found = False
while found == False:
    try:
        guess = int(input('Guess a number 1-100 : '))
        if guess > number:
            print('too HIGH ')
        elif guess < number:
            print('too LOW ')
        elif guess == number:
            print('you got it! ')
            found = True
    except ValueError:
        print('not a valid interger')
print('Thank you for playing. Goodbye.')
