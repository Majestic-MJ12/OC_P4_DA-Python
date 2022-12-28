# the model for the rounds
class RModel:
    def __init__(self, id_round, matches, round_name, time_start, time_end):
        """init of what's going to be stored"""
        self.id_round = id_round
        self.matches = matches
        self.round_name = round_name
        self.time_start = time_start
        self.time_end = time_end
