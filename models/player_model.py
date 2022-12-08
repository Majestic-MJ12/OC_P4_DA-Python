# define the Player class
class PModel:

    def __init__(self, lastname, firstname, birth, gender, score):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score

    def __repr__(self):
        return f"Player({self.lastname!r}, {self.firstname!r}, {self.birth!r}, {self.gender!r}, {self.score!r} ) "

    def win(self):
        self.score += 1

    def tie(self):
        self.score = 0.5

    def lose(self):
        self.score -= 1


# create a list of players
players = [
    PModel("player1", 0),
    PModel("player2", 0),
    PModel("player3", 0),
    PModel("player4", 0),
    PModel("player5", 0),
    PModel("player6", 0),
    PModel("player7", 0),
    PModel("player8", 0),
]
