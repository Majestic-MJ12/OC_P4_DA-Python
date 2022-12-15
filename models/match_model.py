import random
from models.player_model import PModel


class MModel:
    def __init__(self, name, players_duo, winner):
        self.player1 = players_duo[0]
        self.score_player1 = 0
        self.player2 = players_duo[1]
        self.score_player2 = 0
        self.winner = winner
        self.name = name

    def __repr__(self):
        return ([self.player1, self.score_player1],
                [self.player2, self.score_player2])

    def match_playing(self, player):
        if self.score_player1 > self.score_player2:
            self.score_player1 += 1
        elif self.score_player1 < self.score_player2:
            self.score_player2 += 1
        else:
            self.score_player1 += 0.5
            self.score_player2 += 0.5


