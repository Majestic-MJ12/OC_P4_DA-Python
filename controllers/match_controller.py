from models.match_model import MModel
from controllers.player_controller import PController


class MController:
    match_list = []

    def pair_generation(self, cpt_match, match_list):
        """ATTENTION, les joueurs ne doivent pas rejouer 2 fois l'un contre l'autre"""

        if cpt_match % 16 == 1:

            PController.player_rank_sort(PController.players_list)

            for player in range(4):
                match_list.append(MModel.__init__(cpt_match, PController.players_list[player][0], 0,
                                                  PController.players_list[player + 3][0], 0))
                cpt_match = cpt_match + 1
        else:
            PController.player_rank_sort(PController.players_list)

            for player in range(4):
                match_list.append(MModel.__init__(cpt_match, PController.players_list[player][0], 0,
                                                  PController.players_list[player + 1][0], 0))

                cpt_match = cpt_match + 1
        return cpt_match

    def match_result(self, match_list, cpt_match):
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
