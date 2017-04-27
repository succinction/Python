from collections import deque
from random import shuffle

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

rank = {"Ace": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}


card_faces = {
'back': '🂠',
'sa' :'🂡',
's2' :'🂢',
's3' :'🂣',
's4' :'🂤',
's5' :'🂥',
's6' :'🂦',
's7' :'🂧',
's8' :'🂨',
's9' :'🂩',
's1':'🂪',
'sj':'🂫',
'sq':'🂭',
'sk':'🂮',
'ha' :'🂱',
'h2' :'🂲',
'h3' :'🂳',
'h4' :'🂴',
'h5' :'🂵',
'h6' :'🂶',
'h7' :'🂷',
'h8' :'🂸',
'h9' :'🂹',
'h1':'🂺',
'hj':'🂻',
'hq':'🂽',
'hk':'🂾',
'da' :'🃁',
'd2' :'🃂',
'd3' :'🃃',
'd4' :'🃄',
'd5' :'🃅',
'd6' :'🃆',
'd7' :'🃇',
'd8' :'🃈',
'd9' :'🃉',
'd1':'🃊',
'dj':'🃋',
'dq':'🃍',
'dk':'🃎',
'ca' :'🃑',
'c2' :'🃒',
'c3' :'🃓',
'c4' :'🃔',
'c5' :'🃕',
'c6' :'🃖',
'c7' :'🃗',
'c8' :'🃘',
'c9' :'🃙',
'c1':'🃚',
'cj':'🃛',
'cq':'🃝',
'ck':'🃞'}



class Card:
    def __init__(self, s, r, v, f):
        self.rank = r
        self.suit = s
        self.value = v
        self.face = f

    def __str__(self):
        return self.face + " " + self.rank + " of " + self.suit

    def __repr__(self):
        return self.face + " " + self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.cards = deque(self.initialize_deck())

    def __repr__(self):
        return 'Deck: {} {} cards'.format(self.cards, len(self.cards))

    def __str__(self):
        return 'Deck: {} {} cards'.format(self.cards, len(self.cards))

    def initialize_deck(self):
        return [Card(s, r, v, card_faces[s[0].lower() + str(r[0]).lower()]) for s in suits for r, v in rank.items()]

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
        return 'Hand: {} Score: {}'.format(self.cards, self.score())

    def __str__(self):
        return 'Hand: {} Score: {}'.format(self.cards, self.score())

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        ace = 0
        soft = False
        sum =0
        for card in self.cards:
            if "Ace" == card.rank:
                ace += 1
                continue
            else:
                sum += card.value
        if ace > 0:
            for card in self.cards:
                if "Ace" == card.rank:
                    if sum < 10 + ace:
                        soft = True
                        sum += 11
                    else:
                        sum += 1
                else:
                    continue
                    # sum += card.value
        # return sum + (soft * " soft")
        return "{} {}".format(("Soft" if soft else "Hard"), sum)


class Dealer_hand(Hand):
    def __init__(self):
        Hand.__init__(self)

    def __repr__(self):
        return 'Dealer Hand: {} {} {}'.format(" unrevealed card ", self.cards[1:], self.score())

    def __str__(self):
        return 'Dealer Hand: {} {} {}'.format(" unrevealed card ", self.cards[1:], self.score())


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
        for deal_duce in range(2):
            for player, hand in self.table.items():
                self.table[player].add_card(self.deck.deal_card())

    def render_table(self):
        print("#### Game of 21 ####")
        print()
        print("{}".format(self.table["Dealer"]))

        for i in range(self.num_players):
            print("")
            print("{} {}".format( "Player"+str(i), self.table["Player"+str(i+1)]) )



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
player = ''
status = ""
while True:
    g.render_table()
#
    print(status)
#
    play = input("{}, Hit or Hold? ".format(player))
#
    if play.lower() == "hit":
#
        g.table[player].add_card(g.deck.deal_card())
        # player

