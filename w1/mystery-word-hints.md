# Mystery Word

## Variables

- `word_to_guess` - the word the user is trying to guess
- `letters_guessed` - a list of the letters the user has guessed
- `bad_guesses` - the number of bad guesses the user has made

## Some possible functions

`display_word(word, letters)` - returns a string representing the word with the letters in `letters` shown.

> Example: `display_word("bombard", ["b", "d"])` returns `"B _ _ B _ _ D"`

`get_letter_from_user()` - asks the user for a letter and returns that letter as a lowercase letter. If the user enters anything but a letter, give them a warning and ask again.

`get_random_word(difficulty)` - reads the words file, chooses a random word of the correct difficulty

## One approach to solving this

Figure out how to:

1. Get a list of all words from the `words.txt` file.
2. Narrow that list to all words that are between X and Y characters long.
3. Choose one random word from your list.
4. Find out if a certain character is in a word.
5. Display the word with the guessed characters showing.
6. Get user input, prompting them to try again if the input is bad.

Once you've done all that, make an initial version of the game. Don't add too many restrictions -- just have the user give input and then update the display. Once you have that working:

- Stop the user from guessing the same letter multiple times. Warn them if they try and prompt them for another choice.
- Limit the user to eight bad guesses.

Once you have all that, you can add the ability to start again, and you're done!

### How to check to see if your functions work

As you're working on functions, if you want to check and see if they work, you have two options. First, just add some code to your file to run the functions and print some output. That may be a pain, though, if you're working on your program at the same time. In that case, you can start a Python shell by running `python3`. You can cut and paste your functions into this shell. Once you do that, you can run them.
