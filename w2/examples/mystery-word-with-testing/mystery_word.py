def add_to_guesses(word, current_guesses, guessed_letter):
    """
    If guessed letter is in word and not in current guesses,
    add to the guesses. Make sure guessed letter is lowercase.
    """
    if guessed_letter.lower() in word.lower(
    ) and guessed_letter not in current_guesses:
        return current_guesses + [guessed_letter.lower()]


def word_with_guesses(word, guesses):
    """
    Should print the word using underscores for letters not guessed
    and the actual letters for letters in guesses.
    """
    output_list = []
    guesses = [letter.lower() for letter in guesses]
    for letter in word:
        if letter.lower() in guesses:
            output_list.append(letter.upper())
        else:
            output_list.append("_")

    return " ".join(output_list)


def filter_words_by_length(wordlist, min, max):
    return [word for word in wordlist if len(word) in range(min, max + 1)]


def easy_words(wordlist):
    """
    Given a list of words, return just the ones of length 4-6.
    """
    return filter_words_by_length(wordlist, 4, 6)


def medium_words(wordlist):
    """
    Given a list of words, return just the ones of length 6-8.
    """
    return filter_words_by_length(wordlist, 6, 8)
