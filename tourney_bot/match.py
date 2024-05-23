class Match:
    
    def __init__(self, *teams: str) -> None:
        self.score = {team: None for team in teams}

    def is_finished(self) -> bool:
        return all(self.score.values())

    def get_winner(self) -> str:
        if not self.is_finished():
            return
        max_score =  max(self.score.values())
        winners = [team for team, score in self.score.items() if score == max_score]
        if len(winners) > 1:
            return
        return winners[0]
