from typing import Self, Sequence

from textbox import TextBox

class Match:
    
    def __init__(self, teams: Sequence[str], next_match: Self = None) -> None:
        self.teams = list(teams)
        self.scores = [None] * len(teams)
        self.next_match = next_match

    def __str__(self, team_width: int = 8, score_width: int = 3) -> str:
        teams = TextBox.from_list(self.teams, width=team_width)
        scores = TextBox.from_list([score if score else "-" for score in self.scores], align="right", width=score_width)
        return str(teams.join(scores, gap=1))
#…
    def set_score(self, team: str, score: int) -> None:
        i = self.teams.index(team)
        self.scores[i] = score

    def is_finished(self) -> bool:
        if None in self.teams:
            return False
        elif len(self.teams) == 1:
            return True
        elif None in self.scores:
            return False
        return True

    def get_winner(self) -> str:
        if not self.is_finished():
            return
        max_score = max(self.scores)
        winners = [team for team, score in zip(self.teams, self.scores) if score == max_score]
        if len(winners) == 1:
            return winners[0]