def clean_text(text):
    """
    Given a text, return the text with no spaces or punctuation and all lowercased.
    """
    new_text = ""
    text = text.lower()
    # new_text = "".join([char for char in text if char.isalpha()])
    for char in text:
        if char.isalpha():
            new_text = new_text + char
    return new_text



