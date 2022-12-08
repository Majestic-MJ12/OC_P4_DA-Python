# define the Player class
class Player:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player({self.name!r}, {self.score!r})"

    def win(self):
        self.score += 1

    def tie(self):
        self.score = 0.5

    def lose(self):
        self.score -= 1


# create a list of players
players = [
    Player("player1", 0),
    Player("player2", 0),
    Player("player3", 0),
    Player("player4", 0),
    Player("player5", 0),
    Player("player6", 0),
    Player("player7", 0),
    Player("player8", 0),
]
