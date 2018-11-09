# Object-oriented design for Pig

## Description

Design and implement an object-oriented version of the game [Pig](<https://en.wikipedia.org/wiki/Pig_(dice_game)>).

## Objectives

After completing this assignment, you should understand:

- The basics of object-oriented design

After completing this assignment, you should be able to:

- Translate a real-world system into a set of collaborating objects
- Create your own classes
- Instantiate objects from user-defined classes

## Details

### Deliverables

- A Git repo containing at least:
  - a `README.md` file explaining how to run your project
  - a `crc.md` file with your class design
  - a `pig` module
  - a set of tests for each of your classes

### Requirements

- Passing unit tests
- No PEP8 or Pyflakes warnings or errors

## Normal Mode

You are going to implement a version of the game of Pig in Python. Here's how the game works.

Two players are trying to reach 100 points first. On a player's turn, they roll a die over and over until they roll a 1 (a "pig") or they choose to hold. If they hold, they add the sum of their rolls to their score. If they roll a 1, they get no points. After a 1 is rolled or the player holds, the other player takes their turn.

The first player is chosen randomly. (For example, you could flip a coin or both roll a die and pick the higher roll.)

In your implementation, there will be one human player and one computer player. The computer player will always hold until they roll a total of 20 points.

### Design

This game must use Python classes and objects. Before writing any code, sketch out your classes and how they will interact. Each class should have the following listed:

- its name
- its responsibilities -- what are the things this class does? what data does it hold?
- its collaborators -- what other classes does it need to talk to in order to get its job done?

This tool for designing classes is known as the [Class Responsibility Collaborator model](http://agilemodeling.com/artifacts/crcModel.htm) and has been used for many years by expert developers.

Record the CRC model for each of your classes in a file called `crc.md`.

### Development

Once you have these CRC models, you can begin writing code. As you write these classes, you will need to write tests for them using pytest. Because this is a command-line application, I recommend keeping the interface away from the game logic so you can test it in isolation.

### Example game

You do not have to have the same interface or text as this. It is only an example.

```
You will be player 2.
Enter nothing to roll; enter anything to hold.
Player 1 score: 0
Player 2 score: 0
It is player 1's turn.
Roll: 5
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 0
It is player 2's turn.
Roll: 6
Turn total: 6 	Roll/Hold? (Enter)
Roll: 5
Turn total: 11 	Roll/Hold? (Enter)
Roll: 6
Turn total: 17 	Roll/Hold? (Enter)
Roll: 2
Turn total: 19 	Roll/Hold? (Enter)
Roll: 2
Turn total: 21 	Roll/Hold? h
Turn total: 21
New score: 21
Player 1 score: 0
Player 2 score: 21
It is player 1's turn.
Roll: 5
Roll: 6
Roll: 3
Roll: 5
Roll: 1
Turn total: 0
New score: 0
Player 1 score: 0
Player 2 score: 21
It is player 2's turn.
Roll: 6
Turn total: 6 	Roll/Hold? (Enter)
Roll: 6
Turn total: 12 	Roll/Hold? (Enter)
Roll: 2
Turn total: 14 	Roll/Hold? (Enter)
Roll: 6
Turn total: 20 	Roll/Hold? h
Turn total: 20
New score: 41
Player 1 score: 0
Player 2 score: 41
It is player 1's turn.
Roll: 3
Roll: 3
Roll: 6
Roll: 4
Roll: 4
Turn total: 20
New score: 20
Player 1 score: 20
Player 2 score: 41
It is player 2's turn.
Roll: 3
Turn total: 3 	Roll/Hold? (Enter)
Roll: 3
Turn total: 6 	Roll/Hold? (Enter)
Roll: 2
Turn total: 8 	Roll/Hold? (Enter)
Roll: 2
Turn total: 10 	Roll/Hold? (Enter)
Roll: 4
Turn total: 14 	Roll/Hold? (Enter)
Roll: 2
Turn total: 16 	Roll/Hold? (Enter)
Roll: 4
Turn total: 20 	Roll/Hold? h
Turn total: 20
New score: 61
Player 1 score: 20
Player 2 score: 61
It is player 1's turn.
Roll: 5
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 61
It is player 2's turn.
Roll: 3
Turn total: 3 	Roll/Hold? (Enter)
Roll: 3
Turn total: 6 	Roll/Hold? (Enter)
Roll: 5
Turn total: 11 	Roll/Hold? (Enter)
Roll: 2
Turn total: 13 	Roll/Hold? (Enter)
Roll: 6
Turn total: 19 	Roll/Hold? h
Turn total: 19
New score: 80
Player 1 score: 20
Player 2 score: 80
It is player 1's turn.
Roll: 3
Roll: 1
Turn total: 0
New score: 20
Player 1 score: 20
Player 2 score: 80
It is player 2's turn.
Roll: 2
Turn total: 2 	Roll/Hold? (Enter)
Roll: 2
Turn total: 4 	Roll/Hold? (Enter)
Roll: 4
Turn total: 8 	Roll/Hold? (Enter)
Roll: 2
Turn total: 10 	Roll/Hold? (Enter)
Roll: 3
Turn total: 13 	Roll/Hold? (Enter)
Roll: 6
Turn total: 19 	Roll/Hold? (Enter)
Roll: 5
Turn total: 24 	Roll/Hold? h
Turn total: 24
New score: 104
```

## Hard Mode

Some ideas to expand your game:

- Add the ability to play multiple games, alternating the starting player and computing win statistics.
- Add multiple computer players. You can have one that holds at 25, one that always tries to catch up to the other player, or anything else you can think of. When you play, choose a random computer player to play against.

## Additional Resources

- [Object-Oriented Programming in Python 3](https://realpython.com/python3-object-oriented-programming/#what-is-object-oriented-programming-oop)
- [How Do I Design a Class in Python?](https://stackoverflow.com/questions/4203163/how-do-i-design-a-class-in-python) on Stack Overflow
- [The Single Responsibility Principle](https://en.wikipedia.org/wiki/Single_responsibility_principle)
