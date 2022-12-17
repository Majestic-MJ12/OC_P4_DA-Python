from models.match_model import MModel
from controllers.player_controller import PController


class MController:

    def pair_generation(self):
        PController.player_rank_sort(PController.players_list)
        match_list = []
        for combat in range(4):
            match_list = [PController.players_list[combat],
                          PController.players_list[combat+3]]
        return match_list

    def match_result(self, match_list):
        for i in range(4):
            print(match_list[i])
        result = input("Enter the winner number or 0 if tie match: ")
        while result != 0 or 1 or 2:
            result = input("Enter the winner number or 0 if tie match: ")
        MModel.update_scores(result)