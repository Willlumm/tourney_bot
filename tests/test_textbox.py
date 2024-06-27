import pytest

from tourney_bot.textbox import TextBox

@pytest.mark.parametrize(
    argnames = ["text", "expected"],
    argvalues = [
        pytest.param("qwer\nasdf", "\n")
    ]
)
def test_pad():
    TextBox