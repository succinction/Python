cats = 1


def have():
    if cats:
        print("I have cats")
    else:
        print('no cats')


have()

import random

people = ['Malcolm', 'Joe', 'Mike', 'Chase', 'Tab', 'Ian']


def shuff():
    random.shuffle(people)
    # print(people)
    team_a = [people.pop(), people.pop(), people.pop()]
    team_b = people
    print("A: {} \nB: {}  ".format(team_a, team_b))


shuff()

for x in range(2):
    print(x)
