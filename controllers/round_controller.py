from models.round_model import RModel
from controllers.match_controller import MController
from datetime import datetime


class RController:
    rounds_list = [1, 3, "Round1", 12-12-2022, 12-12-2022]

    @staticmethod
    def round_creation(rounds_list):
        cpt_round = len(rounds_list)

        for i in range(1, 5):
            RModel.id_round = cpt_round + 1
            for r in range(len(MController.match_list)):
                RModel.matches = ("Match", MController.match_list[r])

            RModel.round_name = "Round ", cpt_round + 1
            RModel.round_time_start = datetime.strptime
            RModel.round_time_end = datetime.strptime

            rounds = [RModel.id_round, RModel.matches, RModel.round_name,
                      RModel.round_time_start, RModel.round_time_end]
            rounds_list.append(rounds)
            cpt_round = cpt_round + 1
