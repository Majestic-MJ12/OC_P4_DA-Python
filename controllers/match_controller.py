# this is the match controller
# importing what is needed
from models.match_model import MModel
from controllers.player_controller import PController


# the controller for the matches
class MController:
    match_list = []

    def pair_generation(self, cpt_match, match_list):
        """function to generate a battle between two players"""
        """ATTENTION, les joueurs ne doivent pas rejouer 2 fois l'un contre l'autre"""
        players_ids = []
        for i in range(8):
            players_ids.append([i, False])
        already_battle_player = []
        if cpt_match % 16 == 1:
            """verify if it's the first match of the tournament"""
            PController.player_rank_sort(PController.players_list)

            for player in range(4):
                match_list.append(MModel.__init__(cpt_match, PController.players_list[player][0], 0,
                                                  PController.players_list[player + 3][0], 0))
                cpt_match = cpt_match + 1
                already_battle_player.append([player, player + 3])
        else:
            PController.player_score_sort(PController.players_list)

            for player in range(4):
                i = 1
                while [player, player + i] or [player + i, player] or i < 8 in already_battle_player:
                    i = i + 1

                match_list.append(MModel.__init__(cpt_match, PController.players_list[player][0], 0,
                                                  PController.players_list[player + i][0], 0))
                players_ids[player][1] = True
                players_ids[player + i][1] = True

                already_battle_player.append([player, player + i])
                cpt_match = cpt_match + 1

        return cpt_match

    def match_result(self, match_list, cpt_match):
        """function to enter the match results"""
        for i in range(4):
            match = cpt_match - 3 + i
            print(match_list[match])
            result = int(input("Enter the winner player number or 0 if tie match: "))
            while result != 0 or 1 or 2:
                result = int(input("Enter the winner player number or 0 if tie match: "))

            MModel.update_match_scores(match_list[match], result)
            """Player winner : score +1"""
            if result == 1 or 2:
                id_player = result * 2 - 1
                i = 0
                """A VERIFIER"""
                while PController.players_list[i] != match_list[match][id_player]:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 1
            else:
                """Player 1 : score +0.5"""
                id_player = 1
                i = 0
                while PController.players_list[i] != match_list[match][id_player]:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 1
                """Player 2 : score +0.5"""
                id_player = 4
                i = 0
                while PController.players_list[i] != match_list[match][id_player]:
                    i = i + 1
                PController.players_list[i][-1] = PController.players_list[i][-1] + 1
