from math import ceil, log2

from tourney.match import Match
from textbox import TextBox

class Bracket:

    def __init__(self, teams: list[str], match_str_width=10) -> None:
        self.rounds = Bracket.init_bracket(teams)
        self.match_str_width = match_str_width

    def __str__(self) -> str:
        textbox = TextBox()
        line_i0 = 0
        line_di = 4
        lines = [""] * ((4 * (len(self.rounds) ** 2)) - 3)
        block = [""] * ((4 * (len(self.rounds) ** 2)) - 3)
        for round_i, round in enumerate(self.rounds):
            for match_i, match in enumerate(round):
                line_i = line_i0 + line_di * match_i
                block[line_i] += str(match.teams[0])
                block[line_i + 1] += str(match.teams[1])
            line_i0 += line_di // 2
            line_di *= 2
            for i, line in enumerate(block):
                if len(line) > self.match_str_width:
                    line = f"{line[:self.match_str_width - 1]}…"
                lines[i] = line.ljust(self.match_str_width)
        return "\n".join(lines)

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
    def init_bracket(teams: list[str]) -> list[list[Match]]:
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
        rounds.reverse()
        return rounds

    def get_next_match(self) -> Match:
        pass

    def submit_score(self, match: Match) -> None:
        pass

"""
    0  1  2  3

0   0  2  6 14
1   4 10 22
2   8 18
3  12 26

   4  8 16
"""



"""
 0 England  1 _   
 1 Finland  0  |
 2             |_ England  - _
 3             |  Netherl… -  |
 4 Switzer… 1 _|              |
 5 Netherl… 2                 |
 6                            |_ ?        - _
 7                            |  ?        -  
 8 Italy    1 _               |
 9 Slovenia 0  |              |
10             |_ Italy    - _|
11             |  ?        -
12 Austria  - _|
13 Belgium  -
14
15
16 England  1 _   
17 Finland  0  |
18             |_ England  - _
19             |  Netherl… -  |
20 Switzer… 1 _|              |
21 Netherl… 2                 |
22                            |_ ?        -
23                            |  ?        -
24 Italy    1 _               |
25 Slovenia 0  |              |
26             |_ Italy    - _|
27             |  ?        -
28 Austria  - _|
29 Belgium  -
"""