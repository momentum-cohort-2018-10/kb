from mystery_word import word_with_guesses


def test_can_show_word_with_no_guesses():
    assert word_with_guesses("bombard", []) == "_ _ _ _ _ _ _"
    assert word_with_guesses("dog", []) == "_ _ _"


def test_can_show_word_with_guesses():
    assert word_with_guesses("bombard", ['b', 'd']) == "B _ _ B _ _ D"
    assert word_with_guesses("bombard",
                             ['b', 'o', 'm', 'a', 'r', 'd']) == "B O M B A R D"


def test_can_show_word_with_bad_guesses():
    assert word_with_guesses("bombard", ['Y', 'E']) == "_ _ _ _ _ _ _"
    assert word_with_guesses("bombard", ['Y', 'E', 'B']) == "B _ _ B _ _ _"
