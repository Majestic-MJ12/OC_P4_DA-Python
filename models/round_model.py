import datetime
from models.match_model import MModel


class RModel:
    def __init__(self, name, players_pairs, load_match):

        self.name = name
        self.players_pairs = players_pairs

        if load_match:
            self.matches = []
        else:
            self.matches = self.create_matches()

        self.start_date = datetime
        self.end_date = ""

    def __str__(self):
        return self.name

    def create_matches(self):
        matches = []
        for i, pair in enumerate(self.players_pairs):
            matches.append(MModel(name=f"Match {i}", players_duo=pair))
        return matches

    def mark_as_complete(self):
        self.end_date = datetime
        print(f"{self.end_date} : {self.name} over.")
        print("Please enter the match result:")
        for match in self.matches:
            match.match_playing()


