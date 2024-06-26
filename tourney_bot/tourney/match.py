from typing import Self, Sequence

class Match:
    
    def __init__(self, teams: Sequence[str], next_match: Self = None) -> None:
        self.teams = list(teams)
        self.scores = [None] * len(teams)
        self.next_match = next_match

    def __str__(self, width: int = None) -> str:
        width = width if width else 10
        score_width = 3
        team_width = width - score_width
        team_strs = []
        for team, score in zip(self.teams, self.scores):
            team = team[:team_width].ljust(team_width) if team else ""
            score = score if score else "-"
            team_strs.append(f"{team:<10} {score:>}")
        return "\n".join(team_strs)

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