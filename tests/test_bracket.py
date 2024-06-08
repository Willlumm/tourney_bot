import pytest

from tourney_bot.bracket import Match, Bracket

def test_match_set_score():
    match = Match(("a", "b"))
    match.set_score("a", 0)
    assert match.scores == [0, None]

@pytest.mark.parametrize(
    argnames = ["teams", "scores", "expected"],
    argvalues = [
        pytest.param([None], [], False, id="0/1 teams"),
        pytest.param(["a"], [], True, id="1/1 teams"),
        pytest.param([None, None], [], False, id="0/2 teams"),
        pytest.param(["a", None], [], False, id="1/2 teams"),
        pytest.param(["a", "b"], [], False, id="2/2 teams, -:- score"),
        pytest.param(["a", "b"], [0], False, id="2/2 teams, 0:- score"),
        pytest.param(["a", "b"], [0, 0], True, id="2/2 teams, 0:0 score"),
        pytest.param(["a", "b"], [1, 0], True, id="2/2 teams, 1:0 score")
    ]
)
def test_match_is_finished(teams, scores, expected):
    match = Match(teams)
    for team, score in zip(teams, scores):
        match.set_score(team, score)
    assert match.is_finished() == expected

@pytest.mark.parametrize(
    argnames = ["teams", "scores", "expected"],
    argvalues = [
        pytest.param(["a"], [], "a", id="Bye"),
        pytest.param(["a", "b"], [], None, id="Not finished"),
        pytest.param(["a", "b"], [0, 0], None, id="Draw"),
        pytest.param(["a", "b"], [1, 0], "a", id="1:0"),
    ]
)
def test_match_get_winner(teams, scores, expected):
    match = Match(teams)
    for team, score in zip(teams, scores):
        match.set_score(team, score)
    assert match.get_winner() == expected

@pytest.mark.parametrize(
    argnames = ["num_teams", "expected"],
    argvalues= [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (8, 3),
        (9, 4),
        (16, 4),
        (17, 5),
        (32, 5),
        (33, 6),
        (64, 6),
        (65, 7)
    ]
)
def test_bracket_get_num_rounds(num_teams, expected):
    assert Bracket.get_num_rounds(num_teams) == expected

@pytest.mark.parametrize(
    argnames = ["num_teams", "expected"],
    argvalues= [
        (2, [1, 2]),
        (3, [1, None, 2, 3]),
        (4, [1, 4, 2, 3]),
        (5, [1, None, 4, 5, 2, None, 3, None]),
        (8, [1, 8, 4, 5, 2, 7, 3, 6]),
        (9, [1, None, 8, 9, 4, None, 5, None, 2, None, 7, None, 3, None, 6, None]),
        (16, [1, 16, 8, 9, 4, 13, 5, 12, 2, 15, 7, 10, 3, 14, 6, 11])
    ]
)
def test_bracket_arrange_seeds(num_teams, expected):
    assert Bracket.arrange_seeds(num_teams) == expected

@pytest.mark.parametrize(
    argnames = ["teams", "expected"],
    argvalues= [
        (["a"], [("a", None)]),
        (["a", "b"], [("a", "b")]),
        (["a", "b", "c"], [("a", None), ("b", "c")]),
        (["a", "b", "c", "d"], [("a", "d"), ("b", "c")]),
        (["a", "b", "c", "d", "e"], [("a", None), ("d", "e"), ("b", None), ("c", None)]),
        (["a", "b", "c", "d", "e", "f", "g", "h"], [("a", "h"), ("d", "e"), ("b", "g"), ("c", "f")])
    ]
)
def test_bracket_arrange_teams(teams, expected):
    assert Bracket.arrange_teams(teams) == expected

@pytest.mark.parametrize(
    argnames = ["teams", "expected_num_matches"],
    argvalues= [
        (["a"], 0),
        (["a", "b"], 1),
        (["a", "b", "c"], 3),
        (["a", "b", "c", "d"], 3),
        (["a", "b", "c", "d", "e"], 7),
        (["a", "b", "c", "d", "e", "f", "g", "h"], 7),
        (["a", "b", "c", "d", "e", "f", "g", "h", "i"], 15),
        (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"], 15),
        (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"], 31)
    ]
)
def test_bracket_init_matches(teams, expected_num_matches):
    bracket = Bracket(teams)
    assert len(bracket.matches) == expected_num_matches
    assert all(isinstance(match, Match) for match in bracket.matches)
