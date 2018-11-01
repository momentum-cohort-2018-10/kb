def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text = text.lower()
    for character in text:
        if character.isalpha():
            new_text = new_text + character
    return new_text
