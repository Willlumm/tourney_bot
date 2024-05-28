from math import log2
from typing import Self

class Match:
    
    def __init__(self, *teams: str, next_match: Self=None) -> None:
        self.scores = {team: None for team in teams}
        self.next_match = next_match

    def is_finished(self) -> bool:
        if not self.scores:
            return False
        elif len(self.scores) == 1:
            return True
        return all(score is not None for score in self.scores.values())

    def get_winner(self) -> str:
        if not self.is_finished():
            return
        max_score =  max(self.scores.values())
        winners = [team for team, score in self.scores.items() if score == max_score]
        if len(winners) > 1:
            return
        return winners[0]

class Bracket:

    def __init__(self, teams: list[str]) -> None:
        for round in range(len(teams)):
            pass
    
    def __str__(self) -> str:
        pass

    @staticmethod
    def get_num_rounds(num_teams: int) -> int:
        pass

    def get_next_match(self) -> Match:
        pass

    def submit_score(self, match: Match) -> None:
        pass