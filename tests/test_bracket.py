import pytest

from tourney_bot.bracket import Match, Bracket

# Match tests

ids = [
    "0/0 teams",
    "0/1 teams",
    "1/1 teams",
    "0/2 teams",
    "1/2 teams",
    "_:_",
    "0:_",
    "0:0",
    "1:0"
]

match_data = [
    ([], []),
    ([None], []),
    (["a"], []),
    ([None, None], []),
    (["a", None], []),
    (["a", "b"], []),
    (["a", "b"], [0, None]),
    (["a", "b"], [0, 0]),
    (["a", "b"], [1, 0])
]

@pytest.fixture()
def 

@pytest.fixture(params=match_data, ids=ids)
def match_test_cases(request):
    teams, scores = request.param
    match = Match(*teams)
    for team, score in zip(teams, scores):
        match.scores[team] = score
    return match

@pytest.mark.parametrize(("id", "match", "expected"), setup_match_test_cases([True, False, True, False, False, False, False, True, True]))

@pytest.fixture(params=)
def test_match_is_finished(match_test_cases, expected):
    assert match.is_finished() == expected

@pytest.mark.parametrize("expected", [None, None, "a", None, None, None, None, None, "a"])
def test_match_get_winner(expected):
    match = Match(*teams)
    for team, score in zip(teams, scores):
        match.scores[team] = score
    assert match.get_winner() == expected

def test_match_get_winner_not_finished():
    match = Match()
    assert match.get_winner() is None

def test_match_get_winner_draw():
    match = Match("a", "b")
    match.scores["a"] = 0
    match.scores["b"] = 0
    assert match.get_winner() is None

# Bracket tests

def test_bracket_get_num_teams():
    teams = ["1", "2", "3", "4"]
    final_match = Match()
    assert Bracket(teams).matches == [
        Match("1", "4", next_match=final_match),
        Match("2", "3", next_match=final_match),
        final_match
    ]
