name = input('What is your name?: ' )

valid_int=False

while not valid_int:
    try:
        age = int(input('hello {}, how old are you?: '.format(name)))
        valid_int = True
    except ValueError:
        print('not a valid interger')

if  age > 100:
    print('you should be dead by now!')
elif age > 20:
    print('old already?')
else:
    print('Too young')

if  age == 20:
    print('you win')
