
from collections import namedtuple

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

# rank = {"Ace": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}



# Animal = namedtuple('Animal', 'name age type')
# perry = Animal(name="perry", age=31, type="cat")
# print(perry[0])
# Output: perry

Ranks = namedtuple('Ranks', 'Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King')

rank = Ranks(Ace=1, Two=2, Three=3, Four=4, Five=5, Six=6, Seven=7, Eight=8, Nine=9, Ten=10, Jack=10, Queen=10, King=10)












# name = input('What is your name?: ' )
#
# valid_int=False
#
# while not valid_int:
#     try:
#         age = int(input('hello {}, how old are you?: '.format(name)))
#         valid_int = True
#     except ValueError:
#         print('not a valid interger')
#
# if  age > 100:
#     print('you should be dead by now!')
# elif age > 20:
#     print('old already?')
# else:
#     print('Too young')
#
# if  age == 20:
#     print('you win')
