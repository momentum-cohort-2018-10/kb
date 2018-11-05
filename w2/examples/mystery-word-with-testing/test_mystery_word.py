
from mystery_word import word_with_guesses, easy_words, medium_words, add_to_guesses


def test_add_to_guesses_with_correct_letter():
    assert add_to_guesses("bombard", [], "b") == ["b"]
    assert add_to_guesses("bombard", [], "B") == ["b"]
    assert add_to_guesses("bombard", ["d"], "B") == ["d", "b"]


def test_easy_words_filters_list():
    wordlist = [
        "dog", "bombard", "lunch", "candy", "delicious", "sandwich", "fish",
        "carrot"
    ]
    assert easy_words(wordlist) == ["lunch", "candy", "fish", "carrot"]


def test_medium_words_filters_list():
    wordlist = [
        "dog", "bombard", "lunch", "candy", "delicious", "sandwich", "fish",
        "carrot"
    ]
    assert medium_words(wordlist) == ['bombard', 'sandwich', 'carrot']
