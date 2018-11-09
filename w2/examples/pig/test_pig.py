from pig import StopAt20Player, StopAt4RollsPlayer, Game, roll_die


def test_stop_at_20_player_starts_with_0_points():
    player = StopAt20Player()
    assert player.current_score == 0


def test_stop_at_20_player_starts_new_round_with_0_points():
    player = StopAt20Player()
    player.current_score = 12
    player.start_round()
    assert player.current_score == 0


def test_stop_at_20_player_holds_at_20():
    player = StopAt20Player()
    player.start_round()
    player.roll(5)
    player.roll(5)
    player.roll(5)
    assert player.roll_again()

    player.roll(5)
    assert not player.roll_again()


def test_stop_at_4_rolls_starts_with_0_points():
    player = StopAt4RollsPlayer()
    assert player.current_score == 0


def test_stop_at_4_rolls_starts_new_round_with_0_points():
    player = StopAt4RollsPlayer()
    player.current_score = 12
    player.start_round()
    assert player.current_score == 0


def test_stop_at_4_rolls_holds_at_20():
    player = StopAt4RollsPlayer()
    player.start_round()
    player.roll(3)
    player.roll(2)
    player.roll(4)
    assert player.roll_again()

    player.roll(3)
    assert not player.roll_again()


def always_roll_6():
    return 6


def programmable_die(rolls):
    def roll():
        result = rolls.pop(0)
        return result

    return roll


def test_game_round_works():
    game = Game(always_roll_6, StopAt20Player(), StopAt20Player())
    game._current_player = 0
    game.play_round()

    assert game.scores == [24, 0]


def test_game_round_works_if_player_roll_a_1():
    game = Game(
        programmable_die([6, 6, 1]), StopAt20Player(), StopAt20Player())
    game._current_player = 0
    game.play_round()

    assert game.scores == [0, 0]


def test_game_can_play_entire_game():
    game = Game(roll_die, StopAt20Player(), StopAt20Player())
    game.start_game()

    scores = sorted(game.scores)
    assert scores[0] < 100
    assert scores[1] >= 100
