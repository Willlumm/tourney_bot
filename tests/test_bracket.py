from tourney_bot.bracket import Match

# Match tests

def test_is_finished():
    match = Match("team1", "team2")
    match.score["team1"] = 0
    match.score["team2"] = 0
    assert match.is_finished()

def test_is_finished_no_teams():
    match = Match()
    assert not match.is_finished()

def test_is_finished_no_score():
    match = Match("team1", "team2")
    assert not match.is_finished()

def test_is_finished_one_score():
    match = Match("team1", "team2")
    match.score["team1"] = 0
    assert not match.is_finished() 

def test_get_winner():
    match = Match("team1", "team2")
    match.score["team1"] = 0
    match.score["team2"] = 1
    assert match.get_winner() == "team2"

def test_get_winner_not_finished():
    match = Match()
    assert match.get_winner() is None

def test_get_winner_draw():
    match = Match("team1", "team2")
    match.score["team1"] = 0
    match.score["team2"] = 0
    assert match.get_winner() is None

# Bracket tests

def test_generate():
    teams = ["1", "2", "3", "4"]
    expected = []
