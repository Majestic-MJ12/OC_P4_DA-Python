class PModel:
    def __init__(self, id_player, lastname, firstname, birth, gender, score, rank):
        self.id_player = id_player
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score
        self.rank = rank

    def score_player_update(self, points):
        if points == "1":
            self.score = self.score + 1
        elif winner == "2":
            self.score = self.score + 1
        else:
            self.score = self.score + 0.5
            self.score = self.score + 0.5



