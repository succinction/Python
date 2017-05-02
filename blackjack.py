from collections import deque, namedtuple
from random import shuffle

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
Ranks = namedtuple('Ranks', 'Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King')
rank = Ranks(Ace=1, Two=2, Three=3, Four=4, Five=5, Six=6, Seven=7, Eight=8, Nine=9, Ten=10, Jack=10, Queen=10, King=10)

# rank = {"Ace": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10}

card_faces = {
'back': '🂠',
'sac' :'🂡',
'stw' :'🂢',
'sth' :'🂣',
'sfo' :'🂤',
'sfi' :'🂥',
'ssi' :'🂦',
'sse' :'🂧',
'sei' :'🂨',
'sni' :'🂩',
'ste':'🂪',
'sja':'🂫',
'squ':'🂭',
'ski':'🂮',
'hac' :'🂱',
'htw' :'🂲',
'hth' :'🂳',
'hfo' :'🂴',
'hfi' :'🂵',
'hsi' :'🂶',
'hse' :'🂷',
'hei' :'🂸',
'hni' :'🂹',
'hte':'🂺',
'hja':'🂻',
'hqu':'🂽',
'hki':'🂾',
'dac' :'🃁',
'dtw' :'🃂',
'dth' :'🃃',
'dfo' :'🃄',
'dfi' :'🃅',
'dsi' :'🃆',
'dse' :'🃇',
'dei' :'🃈',
'dni' :'🃉',
'dte':'🃊',
'dja':'🃋',
'dqu':'🃍',
'dki':'🃎',
'cac' :'🃑',
'ctw' :'🃒',
'cth' :'🃓',
'cfo' :'🃔',
'cfi' :'🃕',
'csi' :'🃖',
'cse' :'🃗',
'cei' :'🃘',
'cni' :'🃙',
'cte':'🃚',
'cja':'🃛',
'cqu':'🃝',
'cki':'🃞'}


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
        return [Card(s, r, v, card_faces[s[0].lower() + str(r[:2]).lower()]) for s in suits for r, v in rank._asdict().items()]

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

    def score_number(self, softness=False):
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
        if softness:
            return sum, soft
        else:
            return sum

    def add_card(self, card):
        self.cards.append(card)

    def number_named(self, number):
        number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                        'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
                        'twenty']
        pre_number = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        if number < 21:
            return number_names[number]
        else:
            return pre_number[int(str(number)[0])] + number_names[int(str(number)[1])]

    def score(self):
        sum, soft = self.score_number(True)
        return "{} {} {}".format(("Soft" if soft else "Hard"), self.number_named(sum).capitalize(), " BUSTED!" if self.busted() else '')

    def busted(self):
        summ = 0
        for card in self.cards:
            summ += card.value
        return summ > 21


class Dealer_hand(Hand):
    def __init__(self):
        Hand.__init__(self)
        self.playing = False  # "[unrevealed card]"

    def set_playing(self):
        self.playing = True

    def is_playing(self):
        if self.playing:
            return self.cards[0]
        else:
            return "[unrevealed card]"

    def score(self):
        if self.playing:
            sum, soft = self.score_number(True)
            return "{} {} {}".format(("Soft" if soft else "Hard"), self.number_named(sum).capitalize(), " BUSTED!" if self.busted() else '')
            # return self.cards[0]
        else:
            sum = self.cards[1].value
            return "{} {} ".format(self.number_named(sum).capitalize(), " BUSTED!" if self.busted() else '')



    def __repr__(self):
        return 'Dealer Hand: {} {} {}'.format(self.is_playing(), self.cards[1:], self.score())

    def __str__(self):
        return 'Dealer Hand: {} {} {}'.format(self.is_playing(), self.cards[1:], self.score())


class Game21:
    def __init__(self, number_of_players, deck):
        self.num_players = number_of_players + 1
        self.table = self.init_players(number_of_players)
        self.deck = deck
        self.status = ""

    def __repr__(self):
        return 'rpr 21 {} '.format(self.table)

    def __str__(self):
        return 'The Game of 21 \n{} '.format(self.table)

    def init_players(self, num):
        """[0] = dealer"""

        table = {"Player0": Dealer_hand()}
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
        print()
        print("{}".format(self.table["Player0"]))

        for i in range(1, self.num_players):
            print("")
            print("{} {}".format( "Player"+str(i), self.table["Player"+str(i)]))

    def hit(self, player):

        self.table['Player' + str(player)].add_card(self.deck.deal_card())

        if self.table['Player' + str(player)].busted():
            self.status = "Player{} BUSTED!!".format(player)
            return True
        return False
        # self.score(player)
        # pass

    def score(self):
        # IF DEALER BUSTED: GIVE ALL UNBUSTED PLAYERS A WIN, ELSE COMPARE
        winners = []

        if self.table["Player0"].busted():
            for p in range(1, len(self.table)):
                if not self.table["Player"+str(p)].busted():
                    winners.append("Player" + str(p))
        else:
            for p in range(1, len(self.table)):
                if self.table["Player"+str(p)].score_number() > self.table["Player0"].score_number() \
                        and not self.table["Player"+str(p)].busted():
                    winners.append("Player"+str(p))

        print("###################################")
        print("###################################")
        self.render_table()
        print("###################################")
        print("###################################")
        print("########### GAME OVER #############")
        print("###################################")
        print("############ WINNERS: #############")
        if winners != []:
            print(winners)
        elif not self.table["Player0"].busted():
            print("Dealer Won!")
        else:
            pass
        print("###################################")
        quit()

    def status(self):
        return self.status


class GAME:
    # variable = hh

    def __init__(self):
        self.contraband = Deck()
        self.game = Game21(2, self.contraband)
        self.game.deal()
        print(self.game)
        self.player = 1
        # status = ""

    def change_player(self):
        if self.player == 0:
            # DEALER BUSTED, GAME OVER
            self.game.score()

        else:
            self.player = (self.player + 1) % self.game.num_players
            if self.player == 0:
                self.game.table["Player0"].set_playing()

    def run(self):
        while True:
            self.game.render_table()
        #
            print(self.game.status)
        #
            hscore =  self.game.table["Player" + str(self.player)].score_number()
            play = input("\n{}, ({}) \nHit? [enter] or Hold [space + enter]? ({}) ".format('Player' + str(self.player), hscore, hscore))
        #
            if play == "": # hit
                bust = self.game.hit(self.player)
                if bust:
                    self.change_player()
            elif play == ' ':
                self.change_player()
            elif play == 'q' or 'x' == play:
                quit()
            else:
                continue

g = GAME()
g.run()
