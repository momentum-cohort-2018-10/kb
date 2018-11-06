class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def get_score(self):
        if type(self.rank) == int:
            return self.rank
        elif self.rank == "A":
            return 1
        else:
            return 10


class Deck:
    def __init__(self):
        self.cards = []
        for rank in ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']:
            for suit in ['Clubs', 'Spades', 'Diamonds', 'Hearts']:
                self.cards.append(Card(rank, suit))


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def get_score(self):
        has_ace = False
        if "A" in [card.rank for card in self.cards]:
            has_ace = True

        total = sum([card.get_score() for card in self.cards])
        if has_ace and total <= 11:
            total += 10

        return total
