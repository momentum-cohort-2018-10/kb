import textutil


def is_palindrome(text):
    """
    Checks to see if the text is a palindrome.
    Is case-insensitive; ignores punctuation and spaces.
    """
    text = textutil.clean_text(text)

    while len(text) > 1:
        if text[0] == text[-1]:
            text = text[1:-1]
        else:
            return False

    return True


text = input("What text do you want to check to see if it's a palindrome? ")
if is_palindrome(text):
    print("is a palindrome")
else:
    print("is not a palindrome")
