from math import ceil, log2
from typing import Self, Sequence

class Match:
    
    def __init__(self, teams: Sequence[str], next_match: Self = None) -> None:
        self.teams = list(teams)
        self.scores = [None] * len(teams)
        self.next_match = next_match

    def to_str(self, width: int = None) -> str:
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

class Bracket:

    def __init__(self, teams: list[str]) -> None:
        self.matches = Bracket.init_matches(teams)

    def __str__(self) -> str:
        matches = []
        for i, match in enumerate(self.matches):
            matches.append(f"{match.to_str()}")
        return "\n\n".join(matches)

    @staticmethod
    def get_num_rounds(num_teams: int) -> int:
        if num_teams < 2:
            return 0
        return int(ceil(log2(num_teams)))

    @staticmethod
    def arrange_seeds(num_teams: int) -> list[int]:
        seeds = [1, 2]
        for round in range(2, Bracket.get_num_rounds(num_teams) + 1):
            new_seeds = []
            for seed in seeds:
                new_seeds += [seed, 2**round - seed + 1]
            seeds = new_seeds
        return [seed if seed <= num_teams else None for seed in seeds]

    @staticmethod
    def arrange_teams(teams: list[str]) -> list[tuple[str]]:
        seeds = Bracket.arrange_seeds(len(teams))
        arranged_teams = []
        for i in range(0, len(seeds), 2):
            seed1, seed2 = seeds[i : i+2]
            team1 = teams[seed1 - 1] if seed1 else None
            team2 = teams[seed2 - 1] if seed2 else None
            arranged_teams.append((team1, team2))
        return arranged_teams
    
    @staticmethod
    def init_matches(teams: list[str]) -> list[Match]:
        rounds = []
        num_rounds = Bracket.get_num_rounds(len(teams))
        for round_i in range(num_rounds):
            round = []
            team_pairs = [(None, None)] * (2 ** round_i)
            if round_i == num_rounds - 1:
                team_pairs = Bracket.arrange_teams(teams)
            for match_i, team_pair in enumerate(team_pairs):
                match = Match(team_pair)
                if round_i != 0:
                    match.next_match = rounds[round_i - 1][match_i // 2]
                round.append(match)
            rounds.append(round)
        matches = []
        for round in reversed(rounds):
            matches.extend(round)
        return matches


    def get_next_match(self) -> Match:
        pass

    def submit_score(self, match: Match) -> None:
        pass

bracket = Bracket(["really long team name", "b", "c", "d", "e", "f", "g", "h"])
print(bracket)
print(bracket.matches)
