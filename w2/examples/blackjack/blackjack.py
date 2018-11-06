# To make this game:

import random


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
        ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        card = self.cards.pop()
        return card


class Hand:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def get_top_card(self):
        return self.cards[0]

    def is_busted(self):
        return self.get_score() > 21

    def get_score(self):
        has_ace = False
        if "A" in [card.rank for card in self.cards]:
            has_ace = True

        total = sum([card.get_score() for card in self.cards])
        if has_ace and total <= 11:
            total += 10

        return total

    def __str__(self):
        output = ", ".join([str(card) for card in self.cards])
        output += f" ({self.get_score()})"
        return output


class Game:
    def __init__(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deck = Deck()

    def print_player_hand(self):
        print(f"Your hand is {self.player_hand}")

    def print_dealer_hand(self, show_all=False):
        if show_all:
            print(f"The dealer's hand is {self.dealer_hand}")
        else:
            print(
                f"The dealer has {len(self.dealer_hand.cards)} cards. Their top card is {self.dealer_hand.get_top_card()}."
            )

    def ask_player_to_hit(self):
        response = None
        while not (response == "h" or response == "s"):
            if response is not None:
                print("That's not a valid answer!")
            response = input("Do you want to (h)it or (s)tand? ").lower()
        return response == "h"

    def add_card_to_player_hand(self, num=1):
        for _ in range(num):
            self.player_hand.add(self.deck.take_card())

    def dealer_should_hit(self):
        return self.dealer_hand.get_score() < 17

    def play_round(self):
        # On each round:

        # - dealer needs to shuffle cards
        self.deck.shuffle()

        # - dealer needs to deal two cards to the player
        self.add_card_to_player_hand(2)

        self.print_player_hand()

        # - dealer needs to deal two cards to themself
        self.dealer_hand.add(self.deck.take_card())
        self.dealer_hand.add(self.deck.take_card())

        self.print_dealer_hand()

        #   - one dealer card should be face up
        # - while the player wants to hit and the player's hand is not busted
        while self.player_hand.get_score() < 21 and self.ask_player_to_hit():
            #   - add a card to the player's hand
            self.add_card_to_player_hand()
            self.print_player_hand()

        if self.player_hand.is_busted():
            print("You busted!")
            return

        # - while the dealer's hand is < 17
        #   - add a card to the dealer's hand
        while self.dealer_should_hit():
            print("Dealer hits!")
            self.dealer_hand.add(self.deck.take_card())
            self.print_dealer_hand()

        self.print_dealer_hand(show_all=True)

        # - if the dealer is busted, player wins
        if self.dealer_hand.is_busted():
            print("You won!")
            return

        if self.player_hand.get_score() > self.dealer_hand.get_score():
            print("You won!")
        elif self.player_hand.get_score() < self.dealer_hand.get_score():
            print("You lost!")
        else:
            print("You tied!")


if __name__ == "__main__":
    game = Game()
    game.play_round()
