# the model for the matches
class MModel:

    def __init__(self, id_match, player1="", player1_score="", player2="", player2_score=""):
        """init of what's going to be stored"""
        self.id_match = id_match
        self.player1 = player1
        self.player1_score = player1_score
        self.player2 = player2
        self.player2_score = player2_score

    def update_match_scores(self, winner):
        """function to get the scores"""
        if winner == "1":
            self.player1_score = 1
            self.player2_score = 0
        elif winner == "2":
            self.player1_score = 0
            self.player2_score = 1
        else:
            self.player1_score = 0.5
            self.player2_score = 0.5



