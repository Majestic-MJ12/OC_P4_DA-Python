from models.round_model import RModel


class TModel:
    def __init__(self, name="", location="", date_begin="",
                 date_end="", number_of_rounds=4, rounds=None, players=None,
                 time_control="", description=""):
        self.name = name
        self.location = location
        self.date_begin = date_begin
        self.date_end = date_end
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description

    def round_start(self, round_number):
        player_duo = self.players
        round = RModel

