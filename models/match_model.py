# the model for the matches
class MModel:

    def __init__(self, id_match, player1, player1_score, player2, player2_score):
        """init of what's going to be stored"""
        self.id_match = id_match
        self.player1 = player1
        self.player1_score = player1_score
        self.player2 = player2
        self.player2_score = player2_score

    def __str__(self):
        return f"[id_match={self.id_match}, " \
               f"player1={self.player1}, player2={self.player2}, " \
               f"player1_score={self.player1_score}, " \
               f"player2_score={self.player2_score}]"

    def update_match_scores(self, result):
        if result == 1:
            self.player1_score += 1
        elif result == 2:
            self.player2_score += 1
        else:
            self.player1_score += 0.5
            self.player2_score += 0.5



