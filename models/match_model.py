import random
from models.player_model import PModel


# simulate one match
class MModel:
    # randomly choose two players
    player1 = random.choice(PModel.players)
    player2 = random.choice(PModel.players)

    # make sure the players are different
    while player1 == player2:
        player2 = random.choice(PModel.players)

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

