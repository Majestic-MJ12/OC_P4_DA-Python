class PModel:
    def __init__(self, lastname, firstname, birth, gender, score, rank=0):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score
        self.tournament_score = 0
        self.rank = rank
        self.played_with = []

    def __str__(self):
        return f"{self.lastname} {self.firstname} [{self.tournament_score} pts]"
