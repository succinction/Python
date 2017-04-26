from collections import deque
from random import shuffle

suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
rank = {"Ace": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

# rank = {1: "Ace", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 11:"Jack", 12:"Queen", 13:"King"}


class Card:
    def __init__(self, s, r, v):
        self.rank = r
        self.suit = s
        self.value = v

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # self.cards = deque()
        self.cards = deque(self.initialize_deck())

    def __repr__(self):
        return 'Deck: {} {} cards'.format(self.cards, len(self.cards))

    def __str__(self):
        return 'Deck: {} {} cards'.format(self.cards, len(self.cards))

    def initialize_deck(self):

        return [Card(s,r,v) for s in suits for r, v in rank.items()]
        # for s in suits:
        #     for r, v in rank.items():
        #         self.cards.append(Card(s, r, v))

    def shuffle_deck(self):
        print("shuffling deque")
        shuffle(self.cards)
        print(self.cards)

    def deal_card(self):
        return self.cards.popleft()


class Hand:
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return 'Hand: {}'.format(self.cards)

    def __str__(self):
        return 'Hand: {}'.format(self.cards)

    def add_card(self, card):
        self.cards.append(card)


class Dealer_hand(Hand):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'Dealer Hand: {} {} '.format(" unrevealed card ", self.cards[1:])

    def __str__(self):
        return 'Dealer Hand: {} {} '.format(" unrevealed card ", self.cards[1:])


class Game21:
    def __init__(self, number_of_players, deck):
        self.num_players = number_of_players
        self.table = self.init_players(number_of_players)
        self.deck = deck


    def __repr__(self):
        return 'rpr 21 {} '.format(self.table)

    def __str__(self):
        return 'The Game of 21 \n{} '.format(self.table)

    def init_players(self, num):
        """[0] = dealer"""

        table = {"Dealer": Dealer_hand()}
        for i in range(num):
            table["Player" + str(i + 1)] = Hand()
        return table
        # return {"Dealer": Dealer_hand(), "Player1": Hand(), "Player2": Hand()}

    def deal(self):
        self.deck.shuffle_deck()
        for duce in range(2):
            for player, hand in self.table.items():
                self.table[player].add_card(self.deck.deal_card())


#             or
#             hand.add_card(self.deck.deal_card())

    def hit(self):
        pass



# hand1 = Hand()
# hand2 = Hand()
# contraband.shuffle_deck()
# hand.add_card(contraband.deal_card())
# hand.add_card(contraband.deal_card())
# print(hand)
# print()
# print(contraband)

contraband = Deck()
g = Game21(3, contraband)
g.deal()
print(g)




# print(contraband.cards)

