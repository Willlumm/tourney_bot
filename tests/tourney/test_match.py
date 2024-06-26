import pytest

from tourney_bot.tourney.match import Match


def test_set_score():
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
def test_is_finished(teams, scores, expected):
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
def test_get_winner(teams, scores, expected):
    match = Match(teams)
    for team, score in zip(teams, scores):
        match.set_score(team, score)
    assert match.get_winner() == expected