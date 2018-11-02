# Review notes 2018-11-02

```py
# before

player_hand = []
player_hand.append(random.choice(deck))
player_hand.append(random.choice(deck))

dealer_hand = []
dealer_hand.append(random.choice(deck))
dealer_hand.append(random.choice(deck))

# after

player_hand = deal_cards(2)
dealer_hand = deal_cards(2)
show_cards(player_hand)
should_hit = ask_if_user_wants_to_hit()
while should_hit:
  player_hand.append(deal_cards(1))
  show_cards(player_hand)
  should_hit = ask_if_user_wants_to_hit()
```

```py
def print_word(word, prev_choices):
  pass

def play_mystery_word():
  difficulty = ask_user_for_difficulty()
  word = choose_word(difficulty)
  bad_choices = 0
  prev_choices = []
  while bad_choices < 8 and not word_guessed(word, prev_choices):
    print_word(word, prev_choices)
    guess = ask_user_for_letter(prev_choices)
    prev_choices.append(guess)
    if guess not in word:
      bad_choices += 1
      print("you did a bad guess")
    else:
      print("you did a good guess")


play = True
while play:
  play_mystery_word()
  play = input_yn("Do you want to play again?")
```

# Dictionaries and loops

```py
movie_ratings = {
  "Aladdin": 4,
  "The Purge": 5,
  "Venom": 10,
}

for movie in movie_ratings:
  print(movie)

# Aladdin
# The Purge
# Venom

for movie, rating in movie_ratings.items():
  print(movie, rating)

# Aladdin 4
# The Purge 5
# Venom 10

for thing in movie_ratings.items():
  print(thing)
```

## .append

```py
fruits = []
fruits.append('apple')
fruits.append('durian')
fruits.append('pluot')
print(fruits)
```

## Put items in new list

```py
old_list = [....]
new_list = []
for item in old_list:
  if some_test(item):
    new_list.append(item)

names_and_blanks = [
  "Ryan",
  "Charlie",
  "",
  "Oakley",
  "Dallas",
  "",
  "Cadence",
]

only_names = []
for name in names_and_blanks:
  if len(name) > 0:
    only_names.append(name)

# list comprehension
only_names = [name for name in names_and_blanks if len(name) > 0]
name_lengths = [len(name) for name in names_and_blanks if len(name) > 0]
```
