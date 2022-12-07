# define the Player class
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"Player({self.name!r}, {self.score!r})"

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1


