from tourney_bot.match import Match

def test_is_finished():
    match = Match("team1", "team2")
    match.score["team1"] = 1
    match.score["team2"] = 2
    assert match.is_finished() 

def test_is_finished_no_score():
    match = Match("team1", "team2")
    assert not match.is_finished()

def test_is_finished_one_score():
    match = Match("team1", "team2")
    match.score["team1"] = 1
    assert not match.is_finished() 

def test_get_winner():
    match = Match("team1", "team2")
    match.score["team1"] = 1
    match.score["team2"] = 2
    assert match.get_winner() == "team2"

def test_get_winner_no_score():
    match = Match("team1", "team2")
    assert match.get_winner() is None

def test_get_winner_draw():
    match = Match("team1", "team2")
    match.score["team1"] = 0
    match.score["team2"] = 0
    assert match.get_winner() is None
