# the model for the players


class PModel:
    def __init__(self, id_player, lastname, firstname, birth, gender, score, rank):
        """init of what's going to be stored"""
        self.id_player = id_player
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score
        self.rank = rank
