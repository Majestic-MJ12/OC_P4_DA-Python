from models.players_model import Player
import random


# simulate one match
class TwoPlayers:
    # randomly choose two players
    player1 = random.choice(Player.players)
    player2 = random.choice(Player.players)

    # make sure the players are different
    while player1 == player2:
        player2 = random.choice(Player.players)

    # simulate a match and update the scores
    if random.random() < 0.5:
        player1.win()
        player2.lose()
    else:
        player1.lose()
        player2.win()


