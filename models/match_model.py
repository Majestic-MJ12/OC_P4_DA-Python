import random
from models.player_model import PModel


class MModel:
    def __init__(self, first_player="", second_player="", rank=""):
        self.first_player = first_player
        self.second_player = second_player
        self.rank = rank


# simulate one match
class MModelCombat:
    # randomly choose two players
    player1 = random.choice(PModel.players)
    player2 = random.choice(PModel.player)

    # make sure the players are different
    while player1 == player2:
        player2 = random.choice(PModel.player)

    # simulate a match and update the scores
    if random.random() < 0.5:
        player1.win()
        player2.lose()
    elif random.random() == 0.5:
        player1.tie()
        player2.tie()
    else:
        player1.lose()
        player2.win()


match = MModel()

