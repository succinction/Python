suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
rank = {1: "Ace", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"10", 10:"Jack", 10:"Queen", 10:"King"}

# [ace clubs]

class Card:
    def __init__(self, s, r, v):
        self.rank = r
        self.suit = s
        self.value = v

    def __str__(self):
        return rank[self.rank] + " of " + suits[self.suit]

    def __repr__(self):
        return rank[self.rank] + " of " + suits[self.suit]

    # return {"suit": suits[s], "rank": rank[r], "rep": , "look": "[" + rank[r] + "]"}


class Deck:
     def __init__(self):
         self.cards = initialize_deck(self)
         self.deck = []

    def initialize_deck(self):

        for s in suits:
            for v, r in rank.items():
                self.deck.append(Card(s, r, v))

    def shuffle(self):
        pass

    def deal_card(self):
        pass



    # 52 cards


