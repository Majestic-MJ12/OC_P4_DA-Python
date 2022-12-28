# the model for the tournaments
class TModel:

    def __init__(self, id_tournament, name, localisation, date, number_of_rounds, rounds, players,
                 time_control, description):
        """init of what's going to be stored"""
        self.id_tournament = id_tournament
        self.name = name
        self.location = localisation
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
