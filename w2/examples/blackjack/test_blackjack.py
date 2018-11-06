from blackjack import Card, Deck, Hand


def test_create_card():
    card = Card(9, "Clubs")
    assert card.rank == 9
    assert card.suit == "Clubs"


def test_card_to_str():
    card = Card(9, "Clubs")
    assert str(card) == "9 of Clubs"


def test_card_has_a_score():
    card = Card(9, "Clubs")
    assert card.get_score() == 9

    card = Card("Q", "Clubs")
    assert card.get_score() == 10

    card = Card("A", "Clubs")
    assert card.get_score() == 1


def test_card_equality():
    card1 = Card(9, "Clubs")
    card2 = Card(9, "Clubs")
    card3 = Card(3, "Diamonds")
    assert card1 == card2
    assert card1 != card3


def test_new_deck_has_52_cards():
    deck = Deck()
    assert len(deck.cards) == 52


def test_new_deck_has_right_cards_in_it():
    deck = Deck()
    assert Card('Q', 'Hearts') in deck.cards
    assert Card('A', 'Spades') in deck.cards


def test_can_take_card_from_deck():
    deck = Deck()
    deck.shuffle()

    card = deck.take_card()
    assert type(card) is Card
    assert card not in deck.cards


def test_new_hand_has_no_cards():
    hand = Hand()
    assert len(hand.cards) == 0


def test_can_add_card_to_hand():
    hand = Hand()
    hand.add(Card(9, "Clubs"))
    assert len(hand.cards) == 1
    assert Card(9, "Clubs") in hand.cards


def test_hand_to_str():
    hand = Hand()
    hand.add(Card(9, "Clubs"))
    hand.add(Card(3, "Diamonds"))
    assert str(hand) == "9 of Clubs, 3 of Diamonds (12)"


def test_can_calculate_score():
    hand = Hand()
    hand.add(Card(9, "Clubs"))
    hand.add(Card(3, 'Diamonds'))
    assert hand.get_score() == 12


def test_can_calculate_score_with_face_cards():
    hand = Hand()
    hand.add(Card(9, "Clubs"))
    hand.add(Card("J", 'Diamonds'))
    assert hand.get_score() == 19


def test_can_calculate_score_with_aces():
    hand = Hand()
    hand.add(Card(9, "Clubs"))
    hand.add(Card("A", 'Diamonds'))
    assert hand.get_score() == 20
