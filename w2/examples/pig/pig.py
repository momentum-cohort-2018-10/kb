import random


def roll_die():
    return random.randint(1, 6)


class HumanPlayer:
    def __init__(self):
        self.current_score = 0

    def start_round(self):
        self.current_score = 0

    def roll(self, number):
        self.current_score += number

    def roll_again(self):
        response = input("(R)oll or (s)tay?").lower()
        return response[0] == "r"


class StopAt20Player:
    def __init__(self):
        self.current_score = 0

    def start_round(self):
        self.current_score = 0

    def roll(self, number):
        self.current_score += number

    def roll_again(self):
        return self.current_score < 20


class StopAt4RollsPlayer:
    def __init__(self):
        self.current_score = 0
        self.current_rolls = 0

    def start_round(self):
        self.current_score = 0
        self.current_rolls = 0

    def roll(self, number):
        self.current_score += number
        self.current_rolls += 1

    def roll_again(self):
        return self.current_rolls < 4


class Game:
    def __init__(self, die, player1, player2):
        self.die = die
        self.players = [player1, player2]
        self._current_player = None
        self.reset_scores()

    def reset_scores(self):
        self.scores = [0, 0]
        self.round_score = 0

    def pick_random_player(self):
        self._current_player = random.randint(0, 1)
        print(f"Player {self._current_player + 1} starts!")

    def get_current_player(self):
        return self.players[self._current_player]

    def switch_player(self):
        if self._current_player == 0:
            self._current_player = 1
        else:
            self._current_player = 0
        print(f"It is player {self._current_player + 1}'s turn.")

    def game_over(self):
        return self.scores[0] >= 100 or self.scores[1] >= 100

    def start_game(self):
        self.reset_scores()
        self.pick_random_player()

        while not self.game_over():
            self.play_round()
            if not self.game_over():
                self.switch_player()

        print(f"Player {self._current_player + 1} wins!")

    def play_round(self):
        turn_score = 0
        player = self.get_current_player()
        player.start_round()

        roll = self.die()
        player.roll(roll)
        print(f"Roll: {roll}")

        while roll != 1:
            turn_score += roll
            if not player.roll_again():
                break
            roll = self.die()
            player.roll(roll)
            print(f"Roll: {roll}")

        if roll == 1:
            turn_score = 0

        print(f"Turn score: {turn_score}")

        self.scores[self._current_player] += turn_score
        print(
            f"Current score for player {self._current_player + 1}: {self.scores[self._current_player]}"
        )


if __name__ == "__main__":
    game = Game(roll_die, HumanPlayer(), HumanPlayer())
    game.start_game()
